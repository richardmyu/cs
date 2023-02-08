import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status code: ', r.status_code)

response_dict = r.json()

print('Total repositories: ', response_dict['total_count'])

repo_dicts = response_dict['items']

print('Repositories returned: ', len(repo_dicts))
print('\nSelected information about each repository:')

for key in repo_dicts:
    print('\nName: ', key['name'])
    print('Owner: ', key['owner']['login'])
    print('Stars: ', key['stargazers_count'])
    print('Repository: ', key['html_url'])
    print('Description: ', key['description'])
