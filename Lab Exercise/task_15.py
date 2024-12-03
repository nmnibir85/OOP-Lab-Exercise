arr = [10, 5, 15, 20]

try:
    divisor = int(input("Enter a divisor: "))
    for i in range(len(arr)):
        result = arr[i] / divisor
        print(f"{arr[i]} / {divisor} = {result}")
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
