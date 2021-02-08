#1119.Remove vowels from a string
class Solution:
	def removeVowels(self, s: str) -> str:
		return "".join(c for c in s if c not in "aeiou")

"".join(c for c in s if c not in "aeiou")