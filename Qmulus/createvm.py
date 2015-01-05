#!/usr/local/bin/python

from keystoneclient.auth.identity import v2
from keystoneclient import session
from novaclient.client import Client
# from novaclient.exceptions import *
# import novaclient

import settings
import sys, time
 
print settings.OS_AUTH_URL
print settings.OS_USERNAME
print settings.OS_PASSWORD
print settings.OS_TENANT_NAME
print settings.OS_TENANT_ID

print '================ START ================'

retry = 0
auth = v2.Password(auth_url=settings.OS_AUTH_URL,
                   username=settings.OS_USERNAME,
                   password=settings.OS_PASSWORD,
                   tenant_name=settings.OS_TENANT_NAME)
 
sess = session.Session(auth=auth)
nova = Client("2", session=sess)
 
serverlist = nova.servers.list()
# serverlist = nova.servers.findall(name='shihta*')
print 'len(serverlist)=%d' % len(serverlist)

# print type(serverlist[0])
# print dir(serverlist[0])
# print serverlist[0]
# print serverlist[0].hostId
# print serverlist[0].id
# print serverlist[0].status

# for server in serverlist:
#     if server.name.find(settings.NAME_PATTERN_PREFIX % (settings.USER, settings.PROJECT)) >= 0:
#         print server.id, server.hostId, server.status, server.name
#         server.delete()
# sys.exit(0)

# print '======== IP'
# print type(serverlist[0].addresses)
# print serverlist[0].addresses
# print serverlist[0].networks
# # for k, v in serverlist[0].addresses.iteritems():
# #     print k, v
# print '======== IP END'

# print nova.flavors.list()
# print nova.images.list()
# print nova.networks.list()
# print nova.keypairs.list()
# print nova.floating_ip_pools.list()

# fiplist = nova.floating_ips.list()
fiplist = nova.floating_ips.findall(instance_id=None)
print 'len(fiplist) if instance_id == None >> %d' % len(fiplist)

if len(fiplist) > 3:
    for i in range(len(fiplist)-3):
        fiplist[i].delete()
        print '%s deleting' % fiplist[i].ip
sys.exit(0)

# print "len(fiplist)=", len(fiplist)
# print type(fiplist[0])
# print dir(fiplist[0])
# print fiplist[0]

# fip = nova.floating_ips.get()
# fip = nova.floating_ips.create(pool=settings.FIP_POOL)
# print type(fip)
# print dir(fip)
# print fip

image = nova.images.find(name=settings.IMAGE)
flavor = nova.flavors.find(name=settings.FLAVOR)

print '================ START TO CREATE VM'

my_servers = []
for i in xrange(20):
    instance = nova.servers.create(name=settings.NAME_PATTERN % (settings.USER, settings.PROJECT, i), image=image, flavor=flavor, key_name=settings.KEYNAME)
#     instance = nova.servers.find(name=settings.NAME_PATTERN % (settings.USER, settings.PROJECT, i))
#     print type(instance)
#     print dir(instance)
    print instance.name, "creating"
    my_servers.append(instance)

for instance in my_servers:
    fiplist = nova.floating_ips.findall(instance_id=None)
    if len(fiplist) == 0:
        fip = nova.floating_ips.create(pool=settings.FIP_POOL)
        print "new fip=", fip.ip
    else:
        fip = fiplist[0]
        print "old fip=", fip.ip
    while True:
        checkserver = nova.servers.find(id=instance.id)
        if checkserver.status in settings.SERVER_STATUS:
            if checkserver.status == settings.SERVER_STATUS[0]:
                break
            else:
                print 'status = %s, sleep 2s' % checkserver.status
                time.sleep(2)
        else:
            raise Exception("server status error!")
#     time.sleep(2)
#     while retry < settings.RETRY_MAX:
#         try:
#             instance.add_floating_ip(fip.ip)
#         except novaclient.exceptions.BadRequest as e:
#             print 'BadRequest'
#             retry += 1
#             if retry >= settings.RETRY_MAX:
#                 raise Exception("Hit max retry!")
#             time.sleep(1)
    instance.add_floating_ip(fip.ip)
    for secg in settings.SECGROUPS:
        instance.add_security_group(secg)

print '================ START TO CREATE VM END'
