import requests
import json
from pprint import pprint
from secrets import GIT_PAT

# User specified inputs
ORG_NAME    = "travel350"
REPO_REGEX  = "us"
# Fixed inputs
GIT_API_URL = "https://api.github.com"
GITHUB_URL  = "https://github.com"

# Git API headers
headers     = {
    "Authorization": "token "+GIT_PAT,
    "Accept": "application/vnd.github.v3+json"
}

res = requests.get(GIT_API_URL+'/orgs/'+ORG_NAME+'/repos?per_page=10', headers=headers)

res_json = res.json()

# Get the length of JSON and other strings
org_len     = len(ORG_NAME)
gh_url_len  = len(GITHUB_URL)
res_len     = len(res_json)
sum_len     = org_len+gh_url_len+2
# print(sum_len)

for repo_url in res_json:
    # Extract git url from JSON response
    repo_name = repo_url['html_url']
    repo_name = repo_name[sum_len:]
    # Check if required string is part of repo name
    if REPO_REGEX in repo_name:
        print(repo_name)