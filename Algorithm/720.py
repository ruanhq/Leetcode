#720. Longest word in dictionary:
class Solution:
    def longestWord(self, words: List[str]) -> str:
        if words is None or len(words) < 1:
            return ""
        result = ""
        prefix = set("")
        size = 0
        words.sort()
        for word in words:
            if word[:-1] in prefix:
                if len(word) > size:
                    size = len(word)
                    result = word
                prefix.add(word)
        return result



