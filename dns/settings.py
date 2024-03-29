'''
Created on 2011-5-24

@author: stone
'''

# is debug
DEBUG = True

#sys cmd password
SYS_PASSWORD = 'hello'

# master dns server
MASTER_DNS = (
    ('10.103.10.1', 53),
    ('10.103.10.2', 53),
    #('218.108.248.228', 53),
    #('218.108.248.245', 53),
)

# proxy dns server
PROXY_DNS = ('0.0.0.0', 53)

# master dns time out, in seconds
MASTER_DNS_TIMEOUT = 2

# base hosts file
BASE_HOSTS = '../db/hosts.base'
# special hosts directory
HOST_DIR = '../db/hosts/'
# ip directory
IP_DIR = '../db/ips/' 

#message entrance
CMD_SERVER = ('0.0.0.0', 5454)
