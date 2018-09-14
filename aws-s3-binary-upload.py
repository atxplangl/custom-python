#!/opt/python2.7/bin/python2.7
### usage: aws-s3-binary-upload.py <s3 base dir url> <build target.  wild card optional>

### for a given base s3 bucket directory, script will backup current to backup
### copy binary to current for s3 bucket directory path + current
### requirement is to have aws cli installed and configured


### set env variables and pull in libs
import os
import sys

s3_base_dir_url = sys.argv[1]
binary_target = sys.argv[2]

### clean up backup
os.system('aws s3 rm' + " " + s3_base_dir_url + "/backup/" + " " + "--recursive")

### sync current to backup before uploading new binary
os.system('aws s3 sync' + " " + s3_base_dir_url + "/current/" + " " + s3_base_dir_url + "/backup/")

### clean up current before adding new binary
os.system('aws s3 rm' + " " + s3_base_dir_url + "/current/" + " " + "--recursive")

### copy new binary to s3 bucket current for deployment
os.system('aws s3 cp' + " " + binary_target + " " + s3_base_dir_url + "/current/")
