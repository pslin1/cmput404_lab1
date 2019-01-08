#1/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get("http://www.google.com")

print(r.status_code)

s = requests.get("https://raw.githubusercontent.com/pslin1/cmput404_lab1/master/main.py")

print(s.text)
