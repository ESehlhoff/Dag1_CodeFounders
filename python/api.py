print("Start API read application")

import requests
panginaresults = requests.get('https://catfact.ninja/facts')
feitjes = panginaresults.json()

print(feitjes["current_page"])
print(feitjes["data"][0])