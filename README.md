# DeepFuzzer
DeepFuzzer is research project aimed at generating valid CPS models such that it could be used to test CPS tool chains and compiler such as Simulink

### Tech

DeepFuzzer uses open source projects to work properly. Currently the project is an extension of [Clgen]. 
### Installation

DeepFuzzer is tested on Ubuntu 18.04 and CentOS 7.
The project can be built on Windows as well after adaptation of this [script] to compile protocol buffer files. 
The project can be built on [TACC]. Make sure to include <PATH_TO_libcudnn> in LD_LIBRARY_PATH
```sh
$ export LD_LIBRARY_PATH=<PATH_TO_libcudnn>:$LD_LIBRARY_PATH
```

First, create virtual environment using  [Anaconda] so that the installation doesnot conflict with system wide installs.
```sh
$ conda create -n <envname> python=3.6
```

Clone the project and install the dependencies
```sh
$ git clone https://github.com/50417/DeepFuzzTest.git
$ cd DeepFuzzTest
```

Activate environment and Install the dependencies (Change tensorflow tp tensorflow-gpu to use GPU for training).
```sh
$ conda activate <envname>
$ pip install -r requirements.txt
```
Compile protocol buffer files
```sh
$ chmod +x tools/protoc.sh
$ ./tools/proctoc.sh
```
Test your installation 
```sh
$ python clgen.py --config <PATH_TO_CONFIGURATION_FILE>
```
### Support for other programming language
Create a corpus of the programs(training data) and compress it and also define the configuration files. Here is an [ExampleConfigFile] 
### Development

Want to contribute? Great!
DeepFuzzer uses python +  Tensorflow + keras for fast developing.


### Todos

 - Write MORE Tests
 - Add MORE Preprocessors for Mdl files
 - Change the sampling technique


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [clgen]: <https://github.com/ChrisCummins/clgen>
   [script]: <https://github.com/50417/DeepFuzzTest/blob/master/tools/protoc.sh>
   [TACC]: <https://www.tacc.utexas.edu/>
   [Anaconda]: <https://www.anaconda.com/distribution/>
   [ExampleConfigFile]: <https://github.com/50417/DeepFuzzTest/blob/master/clgen/tests/data/Simulink/config.pbtxt>