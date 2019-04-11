import argparse
import requests
from getpass import getpass
import json

def Main():
	parser = argparse.ArgumentParser()


	parser.add_argument("-u","--user", help = "Your usename", action = 'store', default = 'tenshiocelot'), 
	parser.add_argument("-l", "--list-repos", help = "Fetch and lists your repos", action = "store")
	parser.add_argument("-r", "--repos", help = "Fetch your repo and present an stdout", action = "store")
	parser.add_argument("-p", "--pull-requests", help = "Prints open pull requests for repo", action = "store_true")


	args = parser.parse_args()

	def list_repos(user):
		print(f'Hello {user}')
		response = requests.get('https://api.github.com/user/repos', auth=(user, getpass()))
		print("request's status code:", response.status_code)
		json_response = response.json()
		print('Your repos:')
		for i in json_response:
			   print(i['full_name'][len(i['owner']['login']):])

	def repo_info(user,repo):
		print(f'Hello{user}')
		response = requests.get('https://api.github.com/repos/'+user+'/'+repo, auth = (user, getpass()))
		print(response.url)
	
		print("request's status code:", response.status_code)
		print(json.dumps(response.json(), indent = 3))

	def 
	
	print(args)

	list_repos(args.user)

	repo_info(args.user,args.list_repos)

	

	

	#print(args)

if __name__ == '__main__':
	Main()