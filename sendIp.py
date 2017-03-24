import socket
import requests
import sys
import fcntl
import struct

ip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
print ip
url = 'http://ec2-34-195-93-38.compute-1.amazonaws.com:3002/updateIP'
payload = {
    'board': '2',
    'ip': ip
    }

# POST with json
import json
headers = {'content-type': 'application/x-www-form-urlencoded'}
j = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=j)
print r.status_code

sys.exit()
