#Python_Data_Manipulation
tup = 4, 5, 6
nested_tup = ((4, 5, 6), (7, 8))
tuple([4, 0, 2])
tup = tuple("string")
tup[0]
tup = tuple(['foo', [1, 2], True])
tup[2] = False

(4, None, 'foo') + (6, 0) + ('bar',)
('foo', 'bar') * 4

tup = (4, 5, 6)
a, b, c = tup

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

zip(a, b)

for i, j in enumerate(zip(a, b)):
  print(str(i) + str(j))

for i in zip(a, b):
  print(i)

tup = (4, 5, 6)
a, b, c = tup
b

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

a_list = [2, 3, 7, None]
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list[1] = 'peekaboo'
b_list
b_list.insert(1, 'red')
b_list.remove('foo')
a = [7, 2, 5, 1, 3]
a.sort()
a
import bisect 
c = [1, 2, 2, 2, 3, 4, 7]
bisect.bisect(c, 2)
bisect.insort(c, 5)
c2 = [2, 1, 3, 7, 4, 5, 0]
bisect.insort(c2, 2.5)
c2

some_list = ["foo", "bar", "baz"]
mapping = {}
for i, v in enumerate(some_list):
  mapping[v] = i 
mapping



seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
list(zip(seq1, seq2))

for i, (a, b) in enumerate(zip(seq1, seq2)):
  print("{0}: {1}, {2}".format(i, a, b))

list(reversed(range(10)))
empty_dict = {}
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
d1
d1[7] = 'an integer'
d1.pop('dummy')
d1.update({'b': 'foo', 'c': 12})

mapping = dict(zip(range(5), reversed(range(5))))
mapping
hash('string')
hash((1, 2, (2, 3)))


a = {1, 2, 3, 4, 5}
b = {6, 8, 10, 12, 14, 5, 1, 3}
a.union(b)
a & b 
a.intersection(b)
c = a.copy()
c |= b 
d = a.copy()


my_set = {tuple([1, 2, 3,4, 5])}

#Data loading & Storage:






import numpy as np 
import pandas as pd 
df = pd.read_csv("ex1.csv")
pd.read_table("ex2.csv", sep = ",")
list(open('ex3.txt'))
strings = ['a', 'as', 'bat', 'car',
'dove', 'pythob']
[x.upper() for x in strings if len(x) > 2]
set(map(len, strings))

import re
states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south   carolina##', 'West virginia?']

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key = lambda x: len(set(list(x))))
strings

vals = 'a,b, guido'
vals.split(" ")
import pandas as pd
import matplotlib.pyplot as plt 
values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(['apple', 'orange'])
values
dim
#Categorical data:
import numpy as np
import pandas as pd 
values = pd.Series(['apple',
'orange', 'apple', 'apples'] * 2)
pd.unique(values)
pd.value_counts(values)
values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(["apple", "apples"])
dim.take(values)

dim2 = pd.Series(["apple", "apples", "orange"])
dim2.take(values)

#Categorical type in pandas:
fruits = ['apple', 'orange', 'apple', 'apples'] * 2
N = len(fruits)
df = pd.DataFrame({'fruit': fruits,
'basket_id': np.arange(N),
'count': np.random.randint(3, 15, size = N),
'weight': np.random.uniform(0, 4, size = N)},
columns = ['basket_id', "fruit", "count", "weight"])
fruit_cat = df["fruit"].astype("category")
fruit_cat
c = fruit_cat.values
type(c)
df['fruit'] = df["fruit"].astype('category')
df.fruit
myCategories = pd.Categorical(['foo',
'bar', 'baz', 'foo', 'bar'])
myCategories
#make the column as categorical feature.
#Making ordinal features:
categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]
my_cats_2 = pd.Categorical.from_codes(codes, categories)
my_cats_2.as_ordered()

np.random.seed(12345)
draws = np.random.randn(1000)
draws[:5]
pd.qcut(draws, 4)
bins = pd.qcut(draws, 4, labels = ["Q1", "Q2", "Q3", "Q4"])
bins.codes[:10]

bins = pd.Series(bins, name = 'quartile')
results = (pd.Series(draws).
groupby(bins).agg(['count', 'min', 'max']).
reset_index())
results

df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
'value': np.arange(12.)})
df
df.groupby('key').value.mean()
df.groupby('key').value.transform('mean')
df.groupby("key").
g = df.groupby('key').value
g.transform(lambda X: X ** 2)
g.transform(lambda X: X.rank(ascending = False))
def normalize(x):
  return (x - x.mean())/ x.std()
g.apply(normalize)
g.transform(normalize)
normalized = (df['value'] - g.transform('mean'))/ g.transform('std')
#Using the value to do the downstream calculation.
N = 15
times = pd.date_range('2017-05-20 00:00', freq='1min', periods=N)
df = pd.DataFrame({'time': times,
                   'value': np.arange(N)})
df
df.set_index('time').resample('5min').count()
df2 = pd.DataFrame({'time': times.repeat(3),
                    'key': np.tile(['a', 'b', 'c'], N),
                    'value': np.arange(N * 3.)})
df2[:7]

g = df.groupby('key').value
g.transform(lambda X: X ** 2)
g.transform(lambda X: X.rank(ascending = False))

df = load_data()
df2 = df[df['col2'] < 0]
df = pd.DataFrame({'temp_c': [17.0, 25.0]},
index = ['Portland', 'Berkeley'])
df.assign(temp_f = lambda X: X.temp_c * 9/5 + 32)

df.assign(temp_k = lambda X: (X['temp_c'] + 459.67) * 5 / 9)
df
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
  print(key)
dict_iterator = iter(some_dict)
dict_iterator
df.assign(temp_k = lambda X: (X['temp_c'] + 459.67) * 5/ 9)
def squares(n = 10):
  for i in range(1, n + 1):
    yield i ** 2

def squares(n = 10):
  for i in range(1, n + 1):
    yield i ** 2

def squares(n = 10):
  for i in range(1, n + 1):
  	yield i ** 2

squares()
for xx in squares():
  print(xx, end = '   ')

def squares(n = 10):
  for i in range(1, n + 1):
  	yield i ** 2

def csv_reader(file_name):
  for row in open(file_name, "r"):
  	yield row

csv_gen = (row for row in open(file_name))

gen = (x ** 2 for x in range(100))
gen

dict((i, i ** 3) for i in range(10))

float('1.2345')
float('something')

def attempt_float(x):
  try:
    return float(x)
  except ValueError:
    return x

attempt_float(12.3456)

import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
resp

data = resp.json()
data[0]['title']

#Interacting with sql:
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""
con = sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()

#combine and merge datasets:
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
df1
df2

pd.merge(df1, df2)

pd.merge(df1, df2, on = 'key')
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

#merging on index:
left1 = pd.DataFrame({'key': ['a', 'b',
'a', 'a', 'b', 'c'],
'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]},
index = ['a', 'b'])
pd.merge(left1, right1, left_on = 'key', right_index = True)
pd.merge(left1, right1, left_on = 'key', right_index = True,
how = 'outer')

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
df
melted = pd.melt(df, ['key'])
melted.pivot('key', 'variable', 'value')

pd.melt(df, id_vars = ['key'], value_vars = ["B", "C"])

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

pd.melt(df, id_vars = ['A'], value_vars = ['B'])

all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

result = [name for names in all_data 
for name in names if name.count('e') >= 2]

import pandas as pd 
import matplotlib.pyplot as plt 
ser = pd.Series(np.arange(3.))
ser2 = pd.Series(np.arange(3.), index = ['a', 'b', 'c'])
ser2[-1]

df1 = pd.DataFrame(np.arange(12.0).reshape((3, 4)),
columns = list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
columns = list('abcde'))
df2.loc[1, 'b'] = np.nan 
df1 
df2

df = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])
df.add(1)
df.div(10)
df.rdiv(10)
df.rdiv(100)
#Working with time-series in python:

import numpy as np 
import pandas as pd 
from datetime import datetime
now = datetime.now()
now.year, now.month, now.day
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta
delta.days
delta.seconds

from datetime import datetime
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index = dates)
ts

from datetime import datetime 
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
datetime(2011, 1, 7), datetime(2011, 1, 8),
datetime(2011, 1, 10), datetime(2011, 1, 12),
datetime(2012, 2, 7)]
tst = pd.Series(np.random.randn(7), index = dates)

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
  	  	j += 1
  	  k += 1
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

#Data Analysis Example:
from numpy.random import randn
import numpy as np
import os 
import matplotlib.pyplot as plt
import pandas as pd
json_dumps(x)

#import a json file:
import json
path = 'datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]
#get_counts:
def get_counts(sequence):
  counts = {}
  for x in sequence:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
  return counts

from collections import defaultdict
def get_counts2(sequence):
  counts = defaultdict(int)
  for x in sequence:
    counts[x] += 1
  return counts

counts1 = get_counts(time_zones)
counts2 = get_counts(time_zones)

def top_counts(count_dict, n = 10):
  value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
  value_key_pairs.sort()
  return value_key_pairs[-n: ]
top_counts(counts1)

student_tuples = [
('john', 'A', 15),
('jane', 'B', 12),
('dave', 'B', 10)
]
sorted(student_tuples, key = lambda x: x[2])
#By-default, ascending order here.
from collections import Counter
counts3 = Counter(time_zones)
counts.most_common(10)

frames = pd.DataFrame(records)
frames

tz_counts = frames['tz'].value_counts()
subsets = tz_counts[:15]
sns.barplot(x = subsets.index, y = subsets.values)

#usage of argsort:
cframe = frame[frame.a.notnull()]
cframe = cframe.copy()
cframe['os'] = np.where(cframe['a'].str.contains("Windows"),
"Windows", "Not Windows")
cframe['os'][:5]

by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:15]
#nlargest, indexer[-10:]

count_subset = count_subset.stack()
by_tz_os = cframe.groupby(['tz', 'os'])
aggCounts = by_tz_os.size().unstack().fillna(0)
indexer = aggCounts.sum(1).argsort()
indexer[:10]

count_subset = count_subset.stack()
by_tz_os = by_tz_os.size().unstack().fillna(0)

count_subset.name = 'total'
count_subset = count_subset.reset_index()
count_subset[:10]
sns.barplot(x = 'total', y = 'tz', hue = 'os', data = count_subset)

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('datasets/movielens/users.dat', sep = "::", header = None, names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('datasets/movielens/ratings.dat',
sep = "::", header = None, names = rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('datasets/movielens/movie.dat', sep = "::",
header = None, names = mnames)



import pandas as pd 
names1880 = pd.read_csv('datasets/babynames/yob1880.txt',
names = ['name', 'sex', 'births'])
names1880


pd.pivot_table(df, values = 'E', index = ['A', 'C'],
              columns = ["B"], aggfunc = np.sum)
pd.pivot_table(dataFrame, values = col1, index = [col2, col3, col4],
	columns = [col5], aggfunc = np.sum)
#reading in the text data:
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj 
	for vs in re.findall(r'[aeiou]{2, }', word))
fd = nltk.FreqDist(vs for word in wsj
	for vs in re.findall(r'[aeiou]{2, }', word))
'''
^abc: matches some pattern abc at the start of a string
abc$: matches some pattern abc at the end of a string
[abc]: matches one of a set of characters
[A-Z0-9]: matches one of a range of characters
ed|ing|s
*: zero or more of previous items
+: one or more of previous items
?: zero or one of the previous item
$: end of the string
{n}: match exactly n digits
{n, }: match at least n alphabets
{, n}
{m, n}
{, n}
{n, }
a(b|c)+
word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]', word)
len(re.findall(r'[aeiou]', word))
'''
def compress(word):
  pieces = re.findall(regexp, word)
  return ''.join(pieces)

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv 
in re.findall(r'[ptksvr][aeiou]', w)]


arr = np.arange(10)
arr * 4
arr = np.random.randn(4, 3)
arr.mean(0)
demeaned = arr - arr.mean(0)
demeaned.mean(0)
arr - arr.mean(1).reshape((4, 1))

#argsort and lexsort:
values = np.array([5, 0, 1, 3, 2, 4, 7, 8, 6])
indexer = values.argsort()
values[indexer]

first_name = np.array(["Bob", "Jane", "Steve", "Bill", "Barbera"])
last_name = np.array(["Jones", "Arnold", "Arnold", "Jones", "Walters"])
sorter = np.lexsort((first_name, last_name))
#
sorter
list(zip(last_name[sorter], first_name[sorter]))
"""
[('Arnold', 'Jane'), ('Arnold', 'Steve'), 
('Jones', 'Bill'), ('Jones', 'Bob'),
 ('Walters', 'Barbera')]
 #Sort by last_name first followed by sorting by first_name
"""
arr = np.array([0, 1, 7, 12, 15])
arr.searchsorted(9)
#finding element in a sorted array.
arr.searchsorted([0, 8, 11, 16])


data = np.floor(np.random.uniform(0, 10000, size=50))
bins = np.array([0, 100, 1000, 5000, 10000])
data

#Finding the element where insert each element into the new array from the
#current array
bins.searchsorted(data)


import numpy as np 
def mean_distance(x, y):
  n_x = len(x)
  result = 0.0
  count = 0
  for i in range(n_x):
    result += x[i] - y[i]
    count += 1
  return result/ count

x = np.random.randn(100000)
y = np.random.randn(100000)
mean_distance(x, y)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
np.concatenate([arr1, arr2], axis = 0)
np.vstack((arr1, arr2))
np.hstack((arr1, arr2))

arr = np.random.randn(5, 2)
first, second, third = np.split(arr, [1, 3])
#np.split -> 

arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)

arr = np.arange(3)
arr.repeat(4)#repeat each element 4 times.


arr = np.zeros((4, 3))
arr[:] = 5
arr

#reduce:
arr = np.arange(10)
np.add.reduce(arr)
arr.sum()
arr = np.random.randn(5, 5)
arr[::2].sort(1)

arr = np.random.randn(6)
arr.sort()
arr[:, 0].sort()

arr = np.random.randn(5, 5)
arr[:, :-1] < arr[:, 1:]



arr = np.arange(8)
arr.reshape((4, 2)).reshape((2, 4))
arr = np.arange(15)
other_arr = np.ones((3, 5))
other_arr.shape
arr.reshape(other_arr.shape)
arr.flatten()

arr = np.arange(12).reshape((3, 4))
arr.ravel("F")

arr = np.arange(5)
arr.mean(0)
demeaned = arr - arr.mean(0)
demeaned.mean(0)


row_means = arr.mean(1)
row_means.shape
row_means.reshape((4, 1))
demeaned = arr - row_means.reshape((4, 1))
demeaned.mean(1)


arr - arr.mean(1)

arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]


dtype = [('x', np.int64, 3), ('y', np.int32)]
arr = np.zeros(4, dtype=dtype)
arr

arr = np.random.randn(16)
arr.sort(reversed = True)
arr


obj = pd.Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])
obj.drop('c')
#drop element from a series
obj.drop(['d', 'c'])

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
  index = ["Ohio", "Colorado", "Utah", "NewYork"],
  columns = ["One", "Two", "Three", "Four"])
data

obj.drop("c", inplace = True)

obj = pd.Series(np.arange(4.), index = ['a', 'b', 'c', 'd'])
obj['b']

obj['b' : 'c'] = 5
obj
data[data < 5] = 0
data.loc['Colorado', ['Two', 'Three']]

maps1 = defaultdict(str)
maps1 = {"000": 0, "001": 1, "010": 2, "011": 3, "100": 4, "101": 5, "110": 6, "111": 7}

def generateNary(maxValue):
  def generateBinaryUnbiased(p):
    










