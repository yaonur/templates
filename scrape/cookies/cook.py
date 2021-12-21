import requests

response = requests.get('http://www.dev2qa.com')
cookies = response.cookies
for cookie in cookies:
    print('***')
    print(cookie.domain)
    print(cookie.name)
    print(cookie.value)

url='https://www.dev2qa.com'
cookies=dict(name='jerry',password='')