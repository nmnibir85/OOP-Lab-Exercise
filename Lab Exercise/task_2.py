def factorial(n):
    return 1 if n in (0, 1) else n * factorial(n - 1)

n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is:", factorial(n))
