import requests
from bs4 import BeautifulSoup

login_url = ('https://the-internet.herokuapp.com/authenticate')
secure_url = ('https://the-internet.herokuapp.com/secure')

payload = {
    'username': 'tomsmith',
    'password': 'SuperSecretPassword!'
}

with requests.session() as s:
    s.post(login_url, data=payload)
    r = s.get(secure_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())

r = requests.post(login_url, data=payload)

r2 = requests.get(secure_url)
