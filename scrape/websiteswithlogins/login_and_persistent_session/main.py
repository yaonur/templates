from pprint import pprint
import hashlib
import requests
from config import username, password
from bs4 import BeautifulSoup


def get_md5(s):
    return hashlib.md5(bytes(s, encoding='utf8')).hexdigest()


def main(username=username):
    url = 'https://sevashoes.com/en/login'

    with requests.session() as session:
        response = session.post(url, auth=(username, password))
        # pprint(response.text)

        md5_pass = get_md5(password) + ':'
        username = username + ':'

        soup = BeautifulSoup(response.text, 'html.parser')
        challenge = soup.find('input', id='challenge').get('value')
        print(challenge)
        response = get_md5(username + md5_pass + challenge)
        data = {
            'username': username,
            'password': '',
            'challange': '',
            'response': response
        }
        r_post = session.post(url, data=data)

        pprint(r_post.text)
        with open('index.html', 'w') as f:
            f.write(r_post.text)


if __name__ == '__main__':
    main()

