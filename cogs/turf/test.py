import json
import random
import requests

"""with open('/home/koinx/discord/turfbot1/cogs/turf/test.json', 'r') as json_file:
	json_load = json.load(json_file)"""
url = "https://raw.githubusercontent.com/krimbouch07/myrepo/main/turf.json"
data = requests.get(url)
openjs = data.json()

papa = openjs['images'][0]
z = random.choice((papa['url']))
print (z)
