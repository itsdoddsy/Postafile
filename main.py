import requests

url = ""
headers = {'content-type': 'multipart/form-data'}
openfile = open('', 'rb')
filetosend = {'file': openfile}

requests.post(url, files=filetosend)
