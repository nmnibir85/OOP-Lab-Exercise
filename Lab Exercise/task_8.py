# Define the strings
a = "hello"
b = "b2b2b2"
c = "3g3g"

# 1. Concatenate a, b, and c into d
d = a + b + c

# 2. Find the length of d and print d
length_d = len(d)
print("Length of d:", length_d)
print("d:", d)

# 3. Check if "a2" is present in d
if "a2" in d:
    print("'a2' is present in d")
else:
    print("'a2' is not present in d")

# 4. Perform various string operations on d
print("Uppercase:", d.upper())
print("Lowercase:", d.lower())
print("Titlecase:", d.title())
print("Is it all alphanumeric?", d.isalnum())
print("Find '3g':", d.find("3g"))
print("Capitalize:", d.capitalize())
print("Count 'b2':", d.count("b2"))
print("Split:", d.split())
print("Swapcase:", d.swapcase())
print("Strip leading and trailing spaces:", d.strip())
print("Replace 'hello' with 'python':", d.replace("hello", "python"))
