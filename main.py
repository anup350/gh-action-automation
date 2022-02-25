import requests
import json
import base64
import sys
from pprint import pprint

# Pulling GitHub personal access token(PAT) from secrets.py
# The PAT should be authorized by organization to access details of repositories, workflow, users and enterprise.
# NOTE_1: secrets.py has to be created locally and it is gitginored
from secrets import GIT_PAT

# User specified inputs
# Inputs should be specified from command line
# Ex: python3 main.py teampurpose-iac aws
ORG_NAME    = sys.argv[1]
print("Organization name: ",sys.argv[1])

REPO_REGEX  = sys.argv[2]
print("String to match in repo name: ",sys.argv[2])

# Fixed inputs
GIT_API_URL = "https://api.github.com"
GITHUB_URL  = "https://github.com"

# # Encoding token to base64
# GIT_PAT_b64_bytes = base64.b64encode(GIT_PAT.encode("utf-8"))
# GIT_PAT_b64 = str(GIT_PAT_b64_bytes,"utf-8")
# print(GIT_PAT_b64)

# # Decoding token to utf-8
# GIT_PAT_b64_bytes_decode = base64.b64decode(GIT_PAT_b64)
# GIT_PAT_b64_decoded = str(GIT_PAT_b64_bytes_decode, "utf-8")
# print(GIT_PAT_b64_decoded)

# Git API headers
headers     = {
    # "Authorization": "token "+GIT_PAT_b64,
    "Authorization": "token "+GIT_PAT,
    "Accept": "application/vnd.github.v3+json"
}

res = requests.get(GIT_API_URL+'/orgs/'+ORG_NAME+'/repos?per_page=50', headers=headers)

res_json = res.json()

# Get the length of JSON and other strings
org_len     = len(ORG_NAME)
gh_url_len  = len(GITHUB_URL)
res_len     = len(res_json)
sum_len     = org_len+gh_url_len+2
repositories = []

for repo_url in res_json:
    # Extract git url from JSON response
    repo_name = repo_url['html_url']
    repo_name = repo_name[sum_len:]
    # Check if required string is part of repo name
    if REPO_REGEX in repo_name:
        print(repo_name)
        repositories.append(repo_name)