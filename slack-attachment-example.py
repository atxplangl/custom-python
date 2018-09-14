#!/usr/bin/python
# Usage: slack-attachment-example.py <fqdn> <channel>
#  calls gethealthcheck(host,basedir) and post info to slack
#
################################################################################
# -*- coding: utf-8 -*-

import requests
import os
import sys
import json
from gethealthcheck import *

fqdn  = sys.argv[1]
channel  = sys.argv[2]

sdata = gethealthcheck("%(fqdn)s",'/api/v1/healthcheck')%dict(fqdn=fqdn)
ping = (sdata['ping']['healthy'])
sts = (sdata['sts']['healthy'])
services = (sdata['services']['healthy'])
vdata = gethealthcheck("%(fqdn)s",'/api/v1/healthcheck/version')%dict(fqdn=fqdn)
version = (vdata['version'])
productname = (vdata['name'])

url = "https://acxiom-liveramp.slack.com/services/hooks/jenkins-ci/B8mB1oIMiPqlTXq3JZC4Gl06"

payload = "{   \"channel\":\"%(channel)s\",\n    \"attachments\": [\n        {\n            \"color\": \"#36a64f\",\n            \"pretext\": \"%(productname)s\",\n            \"text\": \"deployment to %(fqdn)s\",\n            \"fields\": [\n                {\n                    \"title\": \"version\",\n                    \"value\": \"%(version)s\",\n                    \"short\": true\n                },\n\t\t\t\t{\t\n\t\t\t\t\t\"title\": \"ping healthcheck\",\n                    \"value\": \"%(ping)s\",\n                    \"short\": true\n\t\t\t\t},\n\t\t\t\t{\t\n\t\t\t\t\t\"title\": \"sts healthcheck\",\n                    \"value\": \"%(sts)s\",\n                    \"short\": true\n\t\t\t\t},\n\t\t\t\t{\t\n\t\t\t\t\t\"title\": \"services healthcheck\",\n                    \"value\": \"%(services)s\",\n                    \"short\": true\n\t\t\t\t}\n            ],\n            \"footer\": \"Slack API\",\n            \"footer_icon\": \"https://platform.slack-edge.com/img/default_application_icon.png\"\n        }\n    ]\n}"%dict(ping=ping, sts=sts, services=services,version=version, productname=productname, fqdn=fqdn, channel=channel)
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)

print response.json
