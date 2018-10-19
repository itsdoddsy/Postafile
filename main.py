import requests
import os

url = ""
headers = {'content-type': 'multipart/form-data'}
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
openfile = open(os.path.join(__location__, ''), 'rb')
filetosend = {'file': openfile}

requests.post(url, files=filetosend)
