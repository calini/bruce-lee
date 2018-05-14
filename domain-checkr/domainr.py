import os

# Read original domains
with open("domains.txt", "r") as file:
    domains = [x.strip() for x in file.readlines()]

# Transform in .uk domains
domains = [x.split('.', 1)[0] + '.uk' for x in domains]

#for domain in domains

import requests
requests.get("http://domainr.build/v2/search?query=acme%20cafe")