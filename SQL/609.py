#609.Find Duplicate file in system
#
#["root/a 1.txt(abcd) 2.txt(efgh)",
# "root/c 3.txt(abcd)", 
# "root/c/d 4.txt(efgh)", 
# "root 4.txt(efgh)"]

from collections import defaultdict
class Solution(object):
	def findDuplicate(self, paths):
		result = defaultdict(list)
		temps = []
		#Usage of defaultdict!
		for num in paths:
			files = num.split(" ")
			route = files[0]
			for f in files[1:]:
				first = f.find("(")
				second = f.find(")")
				content = f[first+1: second]
				result[content].append(route + "/" + f[:first])
		ans = []
		for key, value in result.items():
			if len(value) >= 2:
				ans.append(value)
		return ans



#the find in python only return the index first element,
#Here this function returns all the index here.
def find(s, ch):
  return [i for i, ltr in enumerate(s) if ltr == ch]

