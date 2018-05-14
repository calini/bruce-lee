#!/usr/bin/env python3
import requests
import json
import sys
from bs4 import BeautifulSoup as Soup
#shitcoding at it's finest

if len(sys.argv) != 2:
    print("Usage: %s <video id>" % sys.argv[0])
    exit()

api_key = 'AIzaSyCkXKTTWjaZLLXAdAUWP9SiieFTapCn2dE'
request_link = 'https://www.googleapis.com/youtube/v3/videos'

resp = requests.get(request_link, params={'id': sys.argv[1], 'key': api_key, 'part': 'statistics'})
view_count = int(json.loads(resp.content)['items'][0]['statistics']['viewCount'])
print("%d views" % view_count)
