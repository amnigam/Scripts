#!/usr/bin/env python3

import requests
import mmh3
import codecs

url = 'https://www.bhp.com/favicon.ico'

resp = requests.get(url)
favicon = codecs.encode(resp.content,"base64")
hash = mmh3.hash(favicon)

print(hash)
