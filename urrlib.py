import urllib.request
import urllib
import urllib.parse
import json
import gzip


def tutorial_one():
    url = 'https://tr.pinterest.com/resource/BoardPickerBoardsResource/get/?source_url=/search/pins/?q=bira&rs=typed&term_meta[]=bira|typed&data={"options":{"field_set_key":"board_picker","onlyFetchBoards":true,"no_fetch_context_on_resource":false},"context":{}}&_=1637626614143'
    values = {'q': 'python programing tutorials'}
    data = urllib.parse.urlencode(values)
    url = url + data

    # data = data.encode('utf-8')

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X)"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()


def tutorial_two():
    resp = urllib.request.urlopen('https%3A%2F%2Ftr.pinterest.com%2Fresource%2FBoardPickerBoardsResource%2Fget%2F%3Fsource_url%3D%2Fsearch%2Fpins%2F%3Fq%3Dbira%26rs%3Dtyped%26term_meta%5B%5D%3Dbira%7Ctyped%26data%3D%7B%22options%22%3A%7B%22field_set_key%22%3A%22board_picker%22%2C%22onlyFetchBoards%22%3Atrue%2C%22no_fetch_context_on_resource%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D%26_%3D1637626614143')
    # reads page as html this is bytes object
    page_html_bytes = resp.read()
    page_unzipped = gzip.decompress(page_html_bytes)
    page_html_decoded = page_unzipped.decode('utf-8')
    #
    resp.geturl()
    resp.url
    # downlad  html
    urllib.request.urlretrieve(resp.url, 'test.html')  # save file as html
    # page_json=json.load(page_html.decode)
    page_json = json.loads(page_html_decoded.decode('utf-8'))
    # get response 200,401 etc
    resp.getcode()
    # get httplib object it has headers cookies and manymore
    info = resp.info()
    info.items()
    info.keys()


class MyOpener(urllib.request.FancyURLOpener):
    pass


def fanc_url_opener():
    urllib.request.urlopen('http://httpbin.org/user-agent').read()
    # urllib.request.urlopen('http://natas0.natas.labs.overthewire.org')
    urllib.request.get
