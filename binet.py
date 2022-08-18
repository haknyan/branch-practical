from math import sqrt

def binet(n):
	result = (((1+sqrt(5))**n) - ((1 - sqrt(5))**n)) / (2**n * sqrt(5))
	return int(result)

num = int(input())
print(binet(num))
