#!/usr/bin/python
# @(#)	bitbucket_jenkins_hook.py enable stash jenkins web hook for a given repo  
#	Usage: export USER and PASS.  bitbucket_jenkins_hook.py <projectid> <repo>
################################################################################ 
# -*- coding: utf-8 -*-

import requests
import os
import sys
import json

projectid  = sys.argv[1]
repo     = sys.argv[2].lower()
if len(sys.argv) > 3:
    branches = sys.argv[3]
else:
    branches = 'develop release master'

bitbucketurl = ''
jenkinsbaseurl = ''
giturl = "ssh://git@#(bitbucketurl)s:7999/%(projectid)s/%(repo)s.git"%dict(projectid=projectid, repo=repo, bitbucketurl=bitbucketurl)
print giturl
url = "https://(#bitbucketurl)s/rest/api/1.0/projects/%(projectid)s/repos/%(repo)s/settings/hooks/com.nerdwin15.stash-stash-webhook-jenkins:jenkinsPostReceiveHook/enabled"%dict(projectid=projectid, repo=repo, bitbucketurl=bitbucketurl)
print url
payload = "{\n    \"jenkinsBase\": \"http://#(jenkinsbaseurl)s:8080\",\n    \"gitRepoUrl\": \"%(giturl)s\",\n    \"cloneType\": \"ssh\",\n    \"ignoreCerts\": true,\n    \"ignoreCommitters\": \"\",\n    \"branchOptions\": \"\",\n    \"branchOptionsBranches\": \"%(branches)s\"\n}"%dict(giturl=giturl, branches=branches, jenkinsbaseurl=jenkinsbaseurl)
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

user     = os.environ['USER']
secret   = os.environ['PASS']

response = requests.request("PUT", url, verify=False, data=payload, auth=(user,secret), headers=headers)

print response.json
