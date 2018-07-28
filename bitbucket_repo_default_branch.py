#!/usr/bin/python
# @(#)	creates a repo from given project.
#	Usage: export USER and PASS.  bitbucket_repo_default_branch.py <projectid> <repo>
################################################################################ 
# -*- coding: utf-8 -*-

import requests
import os
import sys
import json

projectid  = sys.argv[1]
repo     = sys.argv[2]
bitbucketurl = ''

url = "https://s(bitbucketurl)s/rest/api/latest/projects/%(projectid)s/repos/%(repo)s/branches/default"%dict(projectid=projectid, repo=repo, bitbucketurl=bitbucketurl)
print url

payload = "{\n    \"id\": \"refs/heads/develop\",\n    \"displayId\": \"develop\"\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }
user     = os.environ['USER']
secret   = os.environ['PASS']

response = requests.request("PUT", url, data=payload, auth=(user,secret), headers=headers)

print response.json
