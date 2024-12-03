class InvalidVoterException(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidVoterException("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidVoterException as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter a valid number.")
