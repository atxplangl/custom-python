#!/usr/bin/python
# @(#)	creates a repo from given project.
#	Usage: export USER and PASS.  bitbucket_create_repo.py <projectid> <repo>
################################################################################ 
# -*- coding: utf-8 -*-

import requests
import os
import sys
import json

projectid  = sys.argv[1]
repo     = sys.argv[2]

bitbucketurl = ''

url = "https://%(bitbucketurl)s/rest/api/latest/projects/%(projectid)s/repos/"%dict(projectid=projectid, bitbucketurl=bitbucketurl)
print url

payload = "{\n    \"name\": \"%(repo)s\"\n}"%dict(repo=repo)
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }
user     = os.environ['USER']
secret   = os.environ['PASS']

response = requests.request("POST", url, data=payload, auth=(user,secret), headers=headers)

print response.json
