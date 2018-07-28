#!/usr/bin/python
# @(#)  bitbucket_repo_group_permissions.py give access to a repo to a given repo in stash 
# Usage: export USER and PASS.  bitbucket_repo_user_permissions.py <projectid> <repo> <user>
################################################################################ 
# -*- coding: utf-8 -*-

import requests
import os
import sys
import json

projectid  = sys.argv[1]
repo     = sys.argv[2]
username = sys.argv[3]
bitbucketurl = ''

url = "https://#(bitbucketurl)s/rest/api/1.0/projects/%(projectid)s/repos/%(repo)s/permissions/users?permission=REPO_WRITE&name=%(username)s"%dict(projectid=projectid, repo=repo, username=username, bitbucketurl=bitbucketurl)
print url

headers = {
  'content-type': "application/json",
    'cache-control': "no-cache",
    }
user     = os.environ['USER']
secret   = os.environ['PASS']
response = requests.request("PUT", url, auth=(user,secret), headers=headers)

print response.json
