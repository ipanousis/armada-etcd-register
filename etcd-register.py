#!/usr/bin/python

import re
import os
import etcd
import json

etcd_host = os.environ['ETCD_HOST']
port = 4001
host = etcd_host

if ":" in etcd_host:
  host, port = etcd_host.split(":")

client = etcd.Client(host=host, port=int(port))

try:
  backends = client.read("/backends")
except KeyError:
  client.write("/backends", None, dir=True)

running_containers = json.loads(open('/tmp/containers.json','r').read())['containers']

for running_container in running_containers:
  client.write("/backends/%s/%s" % (running_container['host'], running_container['name']), running_container, ttl=15)

