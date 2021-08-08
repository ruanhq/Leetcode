#html data manipulation
import codecs
f = codecs.open("test.html", "r")
print f.read()

#积累足够之后争取在细分场景进行突破
import requests
import numpy as np 
from bs4 import BeautifulSoup
import pandas as pd 
import requests_cache
import lxml.html as lxl 
import re
from collections import OrderedDict

dic = OrderedDict()
dic.update({"A1": 1})
dic.update({"A2": 2})
dic.update({"A3": 3})
dic.update({"A4": 4})
dic.pop.key(4)



def urls_scraping(base_url = 'https://www.truecar.com/used-cars-for-sale/listings/'):
    urls = []
    pages = []
    for i in range(1, MAX_PAGE + 1):
        pages.append(base_url + "?page=" + str(i))
    for page in pages:
        try:
            response = requests.get(page)
            response.raise_for_status()
        except:
            break
        root = lxl.fromstring(response.content)
        url = ['https://www.truecar.com' + link for link in root.xpath('//div[@data-qa="Listings"]/a/@href')]
        urls += url


import random

