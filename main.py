'''
Created on Feb 15, 2019

@author: dfa
'''
#yay first push
from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=386aa376a85049b9a45c5fb223f1a691')
pprint(r.json())