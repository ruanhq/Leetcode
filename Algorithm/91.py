#91.py 
#decode ways: split the subproblems -> identify the transition equation 
#-> 
#
#
def numDecodings(self, s: str) -> int:
	if len(s) == 0 or s is None:
		return 0
	def search(s: string) -> int:
		if len(string) > 0:
			if string[0] == "0":
				return 0
		if string == "" or len(string) == 1:
			return 1
		if int(string[:2]) <= 26:
			first = search(string[1:])
			second = search(string[2:])
			return first + second 
		else:
			return search(string[1:])

	sumOfDecodingWays = search(s)
	return sumOfDecodingWays


@lru_cache(maxsize = 2)
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)






