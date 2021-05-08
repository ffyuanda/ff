import requests

ngrok_url = 'http://f92f1c74bfb0.ngrok.io'
endpoint = "{}/box-office-mojo-scraper".format(ngrok_url)

r = requests.post(endpoint, json={})
print(r.json()["data"])
