# -*- coding: UTF-8 -*-
import requests
from urllib import request

class CrawlerFun(object):

    def __init__(url):
        _url = url

    def get_req_url_html(self):
        url = self._url
        page = request.urlopen(url)
        html = page.read().decode("utf-8")
        return html

    def get_requests_url_html(self):
        url = self._url
        html = requests.get(url)
        return html.text

    def test(self):
        print ("312")