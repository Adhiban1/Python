import json
from time import sleep

data = {
    "Adhiban": {
        "Upline": "-",
        "downline": [],
        "wallet": 0
    }
}

with open('data.json', 'w') as f:
    f.write(json.dumps(data))
print("Cleared")
sleep(5)