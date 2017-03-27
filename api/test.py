import sys, json

data = {"python": 3, "test": 2, "data": 1}

ships = json.dumps(data)

# simple JSON echo script
for line in sys.stdin:
  print json.dumps(data)
