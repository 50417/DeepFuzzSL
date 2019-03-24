from difflib import SequenceMatcher
from os import walk,path
import os
import argparse
import sys
import datetime
import time
import progressbar

widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
]

class text_diff():

	'''
	#This class checks the difference between two mdkl files 
	Usage: 
	'''

	def __init__(self, score, mode, output_path,file_directory='', file_to_compare='', file_to_compare_with='') -> None:
		"""
		Initializes fileDirectory 
		args: 
		fileDirectory : directory containing all mdl files
		score : Threshold to consider which two file should be considered as duplicate
		mode: Printing modes 

		Returns: 
		None 
		"""
		self.fileDirectory = file_directory
		self.mode = mode
		self.score = score
		self.file_list = []
		self.duplicate_files_dict = {}
		self.file_to_compare = file_to_compare
		self.file_to_compare_with = file_to_compare_with
		self.output_path = output_path

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
			break  # gets the file from the top level directory only

	def compare_files(self, file1, file2) -> None:
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

	def compare_two_files(self) -> float:
		"""
		compares two files given and report similarity score
		args: 
	
		Returns: 
		measure similarity score as a float in the range [0,1]  
				1= Exactly the same 
				0= Entirely different
		"""
		file1 = open(self.file_to_compare_with).read()
		file2 = open(self.file_to_compare).read()
		print(self.compare_files(file1, file2))

	def compare_all_in_dir(self):
		'''
		gets all the files  in a top level directory and compares all of them

		args: 
		None

		returns: 
		a dictionary with the file 
		'''
		duplicate_files = []
		self.get_files_from_directory()

		for f1 in self.file_list:
			#bar = progressbar.progressbar(max_value = 1000, widgets=widgets).start()
			
			# No need to compare duplicate files or create its own dictionary
			if f1 in duplicate_files:
				continue
			bar_counter = 0
			print ("Comparing "+f1 + " with others files")
			file1 = open(self.fileDirectory + "/" + f1).read()
			self.duplicate_files_dict[f1] = []
			for f2 in self.file_list:
				bar_counter+=1
				if f2 in duplicate_files or f2 in self.duplicate_files_dict.keys():
					continue

				file2 = open(self.fileDirectory + "/" + f2).read()
				score = self.compare_files(file1, file2)
				if score == 1.0:
					duplicate_files.append(f2)
					self.duplicate_files_dict[f1].append({f2:score})

				#bar.update(bar_counter)
		return (self.duplicate_files_dict)

	def print_report(self):
		'''
		print list of unique files 
		args: 
		mode :
		unique defaults to unique 


		returns: 
		a dictionary with the file 
		'''
		print("Total number of unique files " +
			  str(len(self.duplicate_files_dict)))
		if (self.mode == 'unique'):
			for key in self.duplicate_files_dict:
				print(key)

		if self.mode == 'duplicate':
			for key, value in self.duplicate_files_dict.items():
				if(len(self.duplicate_files_dict[key]) > 1):
					print("File : " + key)
					print("Duplicates : " + str(value))
	def create_directory(self):
		'''
		creates a directory called results in the current directory or as specified by output_path
		args: 
	

		returns: 
			complete file path along with file name 
			file name: Current date and time upto min and directory where the file to be compared are located .csv
		'''
		file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
		file_path = "results" 
		if(self.output_path is not None):
			file_path = self.output_path + "/results" 
		if(self.fileDirectory[-1]=='/'):
			file_name = file_name +'-'+self.fileDirectory.split('/')[-2]
		else:
			file_name = file_name +'-'+self.fileDirectory.split('/')[-1]

		file_name = file_name+".csv"
		print(file_name)
		#Create Directory 
		access_rights = 0o777
		try: 
			os.mkdir(file_path,access_rights)
		except OSError:
			print("Creation of directory failed | Directory Already Exists")
		return (file_path+"/"+ file_name)

	def save_report(self):
		'''
		saves the comparision results of directory
		args: 
	 
		returns: 
		'''
		
		file_to_open = self.create_directory()
		if(path.isfile(file_to_open)):
			print("File Already Exists")
		else:
			file_to_write = open(file_to_open,"w")
			file_to_write.write('File Name ,Duplicate Files,Similarity Score\n')
			for key, value in self.duplicate_files_dict.items():
				file_to_write.write( key )
				for val in value: 
					for k,v in val.items():
						file_to_write.write( ' ,'+k+','+str(v) +'\n')
				file_to_write.write( '\n' )



			

def main():
	 # Configure the option parser
	usage = "usage: python %prog inputFilePath [inputFilePath2] "
	parser = argparse.ArgumentParser(usage)
	parser.add_argument('-s', '--score', dest="score", type=float,
						help='threshold for comparing two strings ', default=0.8)
	parser.add_argument('-i', '--inputPath', dest="inputPath", type=str,
						help='Input directory path to compare files ')
	parser.add_argument('--inputFile', dest="inputFile", type=str,
						help='Input Files to compare ', nargs=2)
	parser.add_argument('--mode', dest="mode", type=str,
						help='Specify the mode to print results [unique | duplicate ]', default='duplicate')

	parser.add_argument('-o', '--outputPath', dest="outputPath", type=str,
						help='Output csv file (Stores File Duplicates with Score)')
	args = parser.parse_args()
	print("Output File Path :" + str(args.outputPath))
	print("Similarity threshold :" + str(args.score))
	print("Input Path :" + str(args.inputPath))
	print("Input Files: "+ str(args.inputFile))
	if len(sys.argv) == 0:
		parser.print_help()
		sys.exit(1)

	if len(sys.argv) < 1:
		parser.error("need to specify a input File Path")
	if(args.inputPath is not None):
		text_diff_obj = text_diff(args.score, args.mode,args.outputPath,args.inputPath )
		text_diff_obj.compare_all_in_dir()
		text_diff_obj.save_report()
		#text_diff_obj.print_report()
	elif(args.inputFile is not None):
		text_diff_obj = text_diff(args.score, args.mode,args.inputPath,args.inputFile[0],args.inputFile[1] )
		text_diff_obj.compare_two_files()

if __name__ == '__main__':
	main()
