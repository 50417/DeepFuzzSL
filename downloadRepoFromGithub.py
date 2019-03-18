from github import Github
import urllib.request as urllib2
import requests
import os 
from pathlib import Path
class GithubRepoDownload():
	githubURL = "https://github.com"

	def __init__(self):
		self.g = Github('028c403868a7fcdeeebc2a589a32a55c11fd70b0')
		#UPTO 1000 results for each search
		repositories =  self.g.search_repositories(query='Simulink')
		pathToDownload=os.getcwd()
		for repo in repositories:
			linkToDownloadRepo = GithubRepoDownload.githubURL+"/"+repo.owner.login+"/"+ repo.name+"/"+"archive"+"/"+"master.zip"
			#download  file
			response = requests.get(linkToDownloadRepo)
			#Writing to Database SQL ALChemy 

			#Checking if file already exist
			# 
			#saving
			output = open(repo.name+".zip","wb")
			output.write(response.content)
			output.close()

			break


gitObj = GithubRepoDownload()