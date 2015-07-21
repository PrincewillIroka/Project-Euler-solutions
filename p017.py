# 
# Solution to Project Euler problem 17
# by Project Nayuki
# 
# http://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 


ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def to_english(n):
	assert 0 <= n <= 99999
	if n < 100:
		return tens(n)
	else:
		result = ""
		if n >= 1000:
			result += tens(n // 1000) + "thousand"
		if n // 100 % 10 != 0:
			result += ONES[n // 100 % 10] + "hundred"
		if n % 100 != 0:
			result += "and" + tens(n % 100)
		return result


def tens(n):
	if n < 10:
		return ONES[n]
	elif n < 20:
		return TEENS[n - 10]
	else:
		return TENS[n // 10 - 2] + (ONES[n % 10] if n % 10 != 0 else "")


ans = 0
for i in range(1, 1001):
	ans += len(to_english(i))
print(ans)