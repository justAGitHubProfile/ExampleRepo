def factorial(n):
	if n == 1 or n == 2:
		return n
	return factorial(n - 1) + factorial(n - 2)

# Stores the first 10 factorial numbers
first_ten = [factorial(i) for i in range(1, 10)]

print("  ".join(map(str, first_ten)))
