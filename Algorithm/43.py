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

最近拿到paypal 24的offer 觉得对自己的发展是一个非常不错的机会 想跟您这边了解一下关于paypal国内团队的情况，感谢！å
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


    
