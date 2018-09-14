#!/usr/bin/python
# @(#)	get healthcheck info and return data
#	gethealthcheck (host,basepath)
################################################################################
# -*- coding: utf-8 -*-


import requests
import os
import sys
import json

def gethealthcheck(host,basepath):

    url = "http://%(host)s:8080%(basepath)s"%dict(host=host, basepath=basepath)
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data
