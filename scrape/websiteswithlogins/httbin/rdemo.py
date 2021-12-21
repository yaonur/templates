import requests

payload = {'page': 2, 'count': 25}
payload_post={'username':'corey','password':'testing'}
# r = requests.get('https://httpbin.org/get?page=2&count=25')
# r = requests.get('https://httpbin.org/get', params=payload)
# r = requests.post('https://httpbin.org/post', params=payload_post)
r= requests.get ('https://www.instagram.com/')

print(r.text)
