import os

for k, v in os.environ.iteritems():
    if k == "OS_AUTH_URL":
        OS_AUTH_URL = v
    elif k == "OS_USERNAME":
        OS_USERNAME = v
    elif k == "OS_PASSWORD":
        OS_PASSWORD = v
    elif k == "OS_TENANT_NAME":
        OS_TENANT_NAME = v
    elif k == "OS_TENANT_ID":
        OS_TENANT_ID = v

if not (OS_AUTH_URL and OS_USERNAME and OS_PASSWORD and OS_TENANT_NAME and OS_TENANT_ID):
    raise Exception("ENV error!")

FLAVOR = "c1.medium"
IMAGE = "Official_Ubuntu_14.04.1_amd64_linux-image-3.13.0-32-generic"
KEYNAME = "MBA"

USER = 'shihta'
PROJECT = 'swift'
NAME_PATTERN = '%s-%s-%02d'
NAME_PATTERN_PREFIX = '%s-%s-'
FIP_POOL = 'net_external'
SECGROUPS = ['12312port']
RETRY_MAX = 5
SERVER_STATUS = ['ACTIVE', 'BUILD']



