#!/usr/bin/env python

with open('chef-nodes.txt') as f:
    for line in f:
        host = line.split()[3].strip(',')
        platform = line.split()[4].strip()
        version = line.split()[5].strip('.')
        print "Hostname: %s  Platform: %s  OS Version: %s" % (host, platform, version)


