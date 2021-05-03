#shortest word distance:
def shortestDistance(wordsDict: List[str], word1: str, word2: str):
    result = 100000000
    index1 = index2 = 0
    for index, word in enumerate(wordsDict):
        if word == word1:
            index1 = index
            result = min(index1 - index2, result)
        elif word == word2:
            index2 = index 
            result = min(inred2 - index1, result)
    return result


#index, element -> here
index1 = index2 = -1
for index, element in enumerate(lists):
    if word == word1:
        index1 = index
        result = min(result, index1 - index2)
    elif word == word2:
        index2 = index
        result = min(result, index2 - index1)
return result

