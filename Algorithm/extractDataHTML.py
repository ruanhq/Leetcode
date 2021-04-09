#
import urllib2
from bs4 import BeautifulSoup
response = urllib2.urlopen("http://tutorialspoint.com/python/python_overview.htm")
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
for x in soup.find_all('b'):
    print(x.string)

import urllib.request

with urllib.request.urlopen("http://python-data.dr-chuck.net/comments_216543.html") as url:
    s = url.read()
    print(s)

with urllib.request.urlopen("http://python-data.dr-chuck.net/comments_216543.html") as url:
    s = url.read()
    print(s)

soups = BeautifulSoup(s, 'html.parser')
table_rows = soups.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    print(row)

df = pd.DataFrame(pd.read_html(str(soups.find_all("table")))[0])
df.columns = df.iloc[0]
df = df.iloc[1:]

soups = BeautifulSoup(s, 'html.parser')
table_rows = soups.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    print(row)
########

table = soups.find_all('table')
df = pd.DataFrame(pd.read_html(str(table))[0])
df.columns = df.iloc[0]
df = df.iloc[1:]
df

with urllib.request.urlopen("http://python-data.dr-chuck.net/comments_216543.html") as url:
    s = url.read()
    print(s)

########
table = soups.find_all('table')
df = pd.DataFrame(pd.read_html(str(table))[0])
df.columns = df.iloc[0]
df = df.iloc[1:]
df
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    print(row)
###############
import urllib2
from bs4 import BeautifulSoup
response = urllib2.urlopen("http://tutorialspoint.com/python/python_overview.htm")
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

with urllib.request.urlopen("http://python-data.dr-chuck.net/comments_216543.html") as url:
    s = url.read()
    print(s)

table = bs4.BeautifulSoup(html_doc, "html.parser").find_all('table')
df = pd.DataFrame(pd.read_html(str(table))[0])
df.columns = df.iloc[0]
df = df.iloc[1:]
df



#parse json:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

#归并排序:
#O(n * log(n))
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
	    L = arr[:mid]
	    R = arr[mid:]
	    mergeSort(L)
	    mergeSort(R)
	    i = j = k = 0
	    while i < len(L) and j < len(R):
	        if L[i] < R[j]:
	            arr[k] = L[i]
	            i += 1
	        else:
	            arr[k] = R[j]
	            j +=1 
	        k += 1
	    while i < len(L):
	        arr[k] = L[i]
	        i += 1
	        k += 1

	    while j < len(R):
	        arr[k] = R[j]
	        j += 1
	        k += 1

while i < len(L) and j < len(R):
    if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
    else:
    	arr[k] = R[j]
    	j += 1







