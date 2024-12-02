# Define the dictionary
employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),
    45: {5, 6, True, 7, 1}
}

# 1. Print length, type, and dictionary
print("Length of dictionary:", len(employee))
print("Type of dictionary:", type(employee))
print("Dictionary:", employee)

# 2. Access the key employee["type"]["developer"]
developer_skills = employee["type"]["developer"]
print("Developer skills:", developer_skills)

# 3. Change the value of "permanent" to False
employee["permanent"] = False

# 4. Add a new key "gender" with value "male"
employee["gender"] = "male"

# 5. Remove "age" key from dictionary
del employee["age"]

# 6. Use keys(), values(), items()
keys = employee.keys()
values = employee.values()
items = employee.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# 7. Iterate the dictionary using a loop
for key, value in employee.items():
    print(f"Key: {key}, Value: {value}")
