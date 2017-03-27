import sys, json

data = [
    {
            "name": "aircraft-carrier",
            "position": ["a1", "b1", "c1", "d1", "e1"],
            "health": 5,
            "board": "1"
		},
        {
            "name": "cruiser",
            "position": ["a5", "b5"],
            "health": 2,
            "board": "1"
        }
]

ships = json.dumps(data)

# simple JSON echo script
for line in sys.stdin:
    print json.dumps(data)
