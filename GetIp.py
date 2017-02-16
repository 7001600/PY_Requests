# GetIp.py
# Using Requests Module
# 2-15-2017
#
import requests
response = requests.get("http://checkip.amazonaws.com")
print (" ")
print ("Public IP Address:", response.text)
