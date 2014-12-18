#!/usr/bin/python

import os
import etcd
import yaml # yaml to de-serialise JSON, due to JSON de-serialising as unicode rather than string
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

running_containers_string = open('/tmp/containers.json','r').read()
running_containers = yaml.load(running_containers_string)['containers']

for running_container in running_containers:
  client.write("/backends/%s/%s" % (running_container['host'], running_container['name']), running_container, ttl=15)

