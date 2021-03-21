#43. Multiply Strings
def multiply(self, num1, num2):
	result = 0
	carry_1 = 1
	for n_1 in num1[::-1]:
		carry_2 = 1
		for n_2 in num2[::-1]:
			result += (ord(str(n_1)) - ord('0')) * (ord(str(n_2)) - ord('0')) * carry_1 * carry_2
			carry_2 *= 10
		carry_1 *= 10
	return str(result)