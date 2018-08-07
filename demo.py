# -*- coding: UTF-8 -*-
from urllib import request
import requests

def get_url_html(url):
    page = request.urlopen(url)
    html = page.read().decode("utf-8")
    return html


def requests_url_html(url):
    html = requests.get(url)
    return html

if __name__ == "__main__":
    #html = get_url_html("http://www.baidu.com")
    #print(html)

    html = requests_url_html("http://www.baidu.com")
    print(html.text)
