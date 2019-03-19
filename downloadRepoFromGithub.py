from github import Github
import argparse
# import urllib.request as urllib2
import requests
import os
from pathlib import Path


class GithubRepoDownload():
	githubURL = "https://github.com"
	token = "a6b5095eca2ae7d9213ef5851d8702cdba90425e"

	def __init__(self, query, token=None):
		self.gObj = Github(GithubRepoDownload.token)
		# TODOS
		# Argument check if valid
		self.query = query

	def getDownloadLink(self, repo):
		linkToDownloadRepo = GithubRepoDownload.githubURL + "/" + \
			repo.owner.login + "/" + repo.name + "/" + "archive" + "/" + "master.zip"
		return linkToDownloadRepo

	def getRepositoryFromAPI(self):
		 # UPTO 1000 results for each search
		return self.gObj.search_repositories(query=self.query)

	def saveZipFile(self, response, repo_name):
		if not os.path.exists(self.query):
			os.mkdir(self.query)
			print("Directory ", self.query,  " Created ")
		else:
			print("Directory ", self.query,  " already exists")

		filename = self.query + "/" + repo_name + ".zip"
		# Checking if file already exist
		if not os.path.isfile(filename):
			output = open(filename, "wb")
			output.write(response.content)
			output.close()
		else: 
			print("File already exists")

	def downloadAllRepository(self):

		for repo in self.getRepositoryFromAPI():
			# Check the repo Id from the database before downloading

			# download  file
			response = requests.get(self.getDownloadLink(repo))
			# Writing to Database SQL ALChemy

			# saving
			self.saveZipFile(response, repo.name)

			break

parser = argparse.ArgumentParser(description='Get argument for downloading')
parser.add_argument('-q', '--query', dest="query", type=str,
					help='https://help.github.com/en/articles/understanding-the-search-syntax')
parser.add_argument("-t", '--token', dest="token", type=str,
					help='https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line')
args = parser.parse_args()
gitObj = GithubRepoDownload(args.query)
gitObj.downloadAllRepository()
