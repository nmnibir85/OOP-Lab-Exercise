def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
print(f"{num} is a prime number." if is_prime(num) else f"{num} is not a prime number.")
4