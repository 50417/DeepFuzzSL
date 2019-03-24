from difflib import SequenceMatcher
from os import walk
class text_diff():

	'''
	#This class checks the difference between two mdkl files 
	'''
	def __init__(self,fileDirectory) -> None:
		"""
		Initializes fileDirectory 
		args: 
		fileDirectory -- directory containing all mdl files
		
		Returns: 
		None 
		"""
		self.fileDirectory = fileDirectory
		self.file_list = []
		self.duplicate_files_dict ={}

	def get_files_from_directory(self):
		'''
		Gets the file names from the top level directory 
		args:
		None
		Returns: 
		List of file names in that directory
		'''
		for (dirpath, dirnames, filenames) in walk(self.fileDirectory):
			self.file_list.extend(filenames)
			break #gets the file from the top level directory only

	def compare_files(self,file1, file2)  -> None:
		"""
		compares two files given 
		args: 
		file1 : opened first file
		file2 : opened second file
		Returns: 
		measure of the sequences' similarity as a float in the range [0,1]  
			1= Exactly the same 
			0= Entirely different
		"""


		seqMatcher = SequenceMatcher(None, file1, file2)
		return seqMatcher.ratio()

	def compare_all_in_dir(self):
		'''
		gets all the files  in a top level directory and compares all of them

		args: 
		None

		returns: 
		a dictionary with the file 
		'''
		duplicate_files=[]
		self.get_files_from_directory()
		for f1 in self.file_list:
			#No need to compare duplicate files or create its own dictionary
			if f1 in duplicate_files:
				continue
			file1 = open(self.fileDirectory +"/"+ f1).read()
			self.duplicate_files_dict[f1] = []
			for f2 in self.file_list:
			
				file2 = open(self.fileDirectory +"/"+ f2).read()
				score = self.compare_files(file1,file2)
				if score == 1.0:
					duplicate_files.append(f2)
					self.duplicate_files_dict[f1].append(f2)
		return (self.duplicate_files_dict)
	
	def print_report(self, mode = 'unique'):
		'''
		print list of unique files 
		args: 
		mode :
		unique defaults to unique 


		returns: 
		a dictionary with the file 
		'''
		print("Total number of unique files " + str(len(self.duplicate_files_dict)))
		if (mode == 'unique'):
			for key in self.duplicate_files_dict:
				print(key)

		if mode =='duplicate':
			for key,value in self.duplicate_files_dict:
				if(len(self.duplicate_files_dict[key])>1):
					print("File : "+ key)
					print("Duplicates : "+ value)

				


text_diff_obj = text_diff("/Users/sohilshrestha/Desktop/mdl")
text_diff_obj.compare_all_in_dir()
text_diff_obj.print_report('duplicate')
