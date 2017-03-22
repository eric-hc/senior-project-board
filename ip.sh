#!/bin/bash
ip = $(/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: | awk '{print $1}')
echo $ip

