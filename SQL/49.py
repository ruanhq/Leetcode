#49. Group Anagrams:
#What's the key -> different anagrams share the same key.(count of different words are constant)
class Solution(object):
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = collections.defaultdict(list)
    for s in strs:
      result[tuple(sorted(s))].append(s)
    return result.values()

class Solution(object):
  def groupAnagram(self, strs: List[str]) -> List[List[str]]:
  	result = collections.defaultdict(list)
  	for s in strs:
  		count = [0] * 26
  		for c in s:
  		    count[ord(c) - ord("a")] += 1
  		result[tuple(count)].append(s)
  	return result.values()