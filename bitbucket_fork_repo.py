#!/usr/bin/python
# @(#)	stash_fork_repo.py	fork repository from given project and give a name.  
#	Usage: export USER and PASS.  bitbucket_fork_repo.py <projectid> <repo> <name>
################################################################################ 
# -*- coding: utf-8 -*-

import requests
import os
import sys
import json

projectid  = sys.argv[1]
repo     = sys.argv[2]
forkname = sys.argv[3]
bitbucketurl = ''

url = "https://#(bitbucketurl)s/rest/api/latest/projects/%(projectid)s/repos/%(repo)s"%dict(bitbucketurl=bitbucketurl,projectid=projectid, repo=repo)
print url
payload = "{\"name\":\"%(forkname)s\", \"project\": {\"key\": \"%(projectid)s\"}}"%dict(forkname=forkname, projectid=projectid)
print payload
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }
user     = os.environ['USER']
secret   = os.environ['PASS']
response = requests.request("POST", url, data=payload, auth=(user,secret), headers=headers)

print response.json

