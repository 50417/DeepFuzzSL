"""Simulink preprocessor passes."""
from absl import flags

from clgen import errors
from clgen.preprocessors import public
import re
import string

FLAGS = flags.FLAGS
class CollectedToken:

    @property
    def output(self):
        if self._is_post_process_on and self.kw in POST_PROCESSOR_REGISTRY:
            return POST_PROCESSOR_REGISTRY[self.kw]().go(self)
        else:
            return ''.join(self.outputs)

    def __init__(self, kw, init_line='', is_post_process_on=False):
        self._is_post_process_on = is_post_process_on
        self.kw = kw  # The keyword
        self.outputs = [init_line]
        self.brace_count = 1

    def add_line(self, line):
        # Line may not be string in case of post-processors present
        self.outputs.append(line)
DUMMY_MODEL_ROOT = 'SLearnerDummyRoot'
_collectibles = [{
            DUMMY_MODEL_ROOT: {'Model': {
                'Name': None,  # None means capture the whole element
                'System': {
                    'Block': None,
                    'Line': None,
                    None: None  # Also collect others type of children
                }
            }}
        }, ]  # Stack

_collections = [CollectedToken(DUMMY_MODEL_ROOT)] 
         # Stack containing collected tokens.



def get_sl_tokens(line:str)->str:
  """Private helper method to get token of simulink mdl line.

  Args:
    text: The single line of  mdl file

  Returns:
    src: tokens in each line.

  Raises:
    
  """

  return re.split(r'\s|(?<!\d)[,.](?!\d)', line)

def _include_line( line, original_line, tokens, top):
    # Return: whether to add token in unique keywords

        if line == "}":
            top.add_line(original_line)
            top.brace_count -= 1

            if top.brace_count == 0:
                _decrement_scope(top)

            return

        has_open_brace = "{" in tokens
        
        if not has_open_brace:
            # Single liners -- no need to start new scope.
            top.add_line(original_line)

        elif _collectibles[-1][top.kw] is None:
            # Parent wants every child. No need to start scope, instead use brace counting
            top.add_line(original_line)
            top.brace_count += 1
        else:
            # Parent wants selected children. Start new scope
            _collectibles.append(_collectibles[-1][top.kw])
            _collections.append(CollectedToken(tokens[0], original_line))


def _skip_line( line, original_line, tokens, top):
        """ This keyword is not interesting.
        Just do brace count to know when to return from scope."""

        if line == '}':
            top.brace_count -= 1

            if top.brace_count == 0:
                top.add_line(original_line)
                top.add_line("\n")
                _decrement_scope(top)
            else:  # Still non-interesting
                _collectibles.pop()

        elif '{' in tokens:
            top.brace_count += 1
            _collectibles.append(None)  # Dummy

def _decrement_scope( top):
        """Pop Elements from various stacks due to decrementing scope"""
        _collectibles.pop()
        _collections.pop()
        _collections[-1].add_line(top.output)

@public.clgen_preprocessor
def StripDuplicateWhiteSpaces(text: str) -> str:
  """
  Extra WhiteSpaces removed between Keywords and  and its assignment
  Args:
    text: The Simulink MdlFile source to preprocess.
  Returns:
    Simulink source code with middle or duplicate whitespaces stripped
  """
  last_line = None
  lines = []
  for line in text.split("\n"):
    line = line.replace(" \t","  ")
    line = re.sub("\s\s+"," ",line.lstrip())
    lines.append(line) 
  return "\n".join(lines)

@public.clgen_preprocessor
def RemoveUnnecessaryOnSimulink(text: str) -> str:
  """
  Remove Unnecessary keywords
  Args:
    text: The Simulink MdlFile source to preprocess.
  Returns:
    Simulink source code with Unnecessary keywords removed
    """
  lines = []
  count = 0
  for line in text.split("\n"):
        removeList = ["Location","Open", "Points","ZOrder","Position", "ICPrevOutput", "LibraryVersion","SourceType","SourceProductName", "DelayOrder","ContentPreviewEnabled","SourceProductBaseCode","ICPrevScaledInput","OutDataTypeStr","InputProcessing", "OutputDataTypeScalingMode","InitialConditionSetting","PortBlocksUseCompactNotation", "ModelBrowserVisibility",  "ModelBrowserWidth",      "ScreenColor",        "PaperOrientation",    "PaperPositionMode",    "PaperType",        "PaperUnits",       "TiledPaperMargins",     "TiledPageScale",    "ShowPageBoundaries",  "ZoomFactor",       "ReportName"]  
        #removeList = ["Location","Open","ZOrder",     "PortBlocksUseCompactNotation", "ModelBrowserVisibility",  "ModelBrowserWidth",      "ScreenColor",        "PaperOrientation",    "PaperPositionMode",    "PaperType",        "PaperUnits",       "TiledPaperMargins",     "TiledPageScale",    "ShowPageBoundaries",  "ZoomFactor",       "ReportName"]  
        line = line.lstrip()
        if line.startswith(tuple(removeList)):
            continue
        lines.append(line)
  return "\n".join(lines)


@public.clgen_preprocessor
def interLeaveBlocksandLines(text:str)->str:
  """InterLeave Blocks Blocks and Lines connecting them.

    Args:
    text: The source mdl files

  Returns:
    src: The modified input src with interleaving Line and Block.

  Raises:
    
  """
  for l in text.splitlines():
      line= l.strip()
      tokens = get_sl_tokens(line)
  
      top = _collections[-1]
      lookup = _collectibles[-1] # Top of collectibles
      if lookup is not None and (lookup[top.kw] is None or tokens[0] in lookup[top.kw] or None in lookup[top.kw]):
        _include_line(line, l, tokens, top)  # This may change top by pushing new
      else:
        _skip_line(line, l, tokens, top)
  return _collections[-1].output

def getTokens(line): 
  return re.split(r'[\s]+', line)

@public.clgen_preprocessor
def RenameModelName(text:str)->str:
  """Rename all MOdel Names to sample.

  Args:
    text: The source mdl files

  Returns:
    src: The modified input with Model name renamed to sample.
 
  Raises:
    
  """
  modelFlag = 1
  lines = []
  for line in text.split("\n"):
    tokens = getTokens(line)
    line = line.lstrip()
    if('Model' in tokens):
      modelFlag = 0
    elif('Name' in tokens and modelFlag==0):
      text = text.replace(tokens[1],"\"sample\"")
      break
  return text

def collectBlockNames(text:str):
  blockFlag = 1
  setOfNames = []
  duplicate={}
  for line in text.split("\n"):
    line = line.strip()
    tokens = getTokens(line)
    if('Block' in tokens):
      blockFlag = 0
    elif('Name' in tokens and blockFlag==0):
      if tokens[1] not in duplicate:
        duplicate[tokens[1]]=tokens[1]
        setOfNames.append(tokens[1])
  return setOfNames

@public.clgen_preprocessor
def RenameBlockNames(text:str)->str:
  """Rename all blocks Names to ASCII characters .
  Need work when there are more variable than ASCII characters
  Need TEST cases and exceptions

  Args:
    text: The source mdl files

  Returns:
    src: The modified input with Block name renamed .
 
  Raises:
    
  """
  blockNames = collectBlockNames(text)
  i = 0 
  for name in blockNames:
      #print(str(i)+" "+name+" " +string.ascii_letters[i])
      text = text.replace(name,"\""+string.ascii_letters[i]+"\"")
      i=i+1


  return text 

@public.clgen_preprocessor
def SetSIDtoDetfault(text:str)->str:
  """Sets SIDHighWatermark to "1"

  Args:
    text: The source mdl files

  Returns:
    src: The modified input with SIDHighWatermark set to "1"
 
  Raises:
    
  """
  for line in text.split("\n"):
    tokens = getTokens(line)
    line = line.lstrip()
    if('SIDHighWatermark' in tokens):
      text = text.replace(tokens[1],"\"1\"")
      break
  return text