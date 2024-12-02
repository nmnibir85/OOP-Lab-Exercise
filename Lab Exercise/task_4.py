a = [1, 3, 5, 7, 9]
print("Initial list:", a)

# Accessing elements
print("a[-2]:", a[-2])  # Second last element
print("a[2]:", a[2])    # Third element
print("Length of the list:", len(a))

# Modifying list
a[3], a[2] = 50, 19
a.append(100)
a.insert(2, 200)
a.pop()  # Remove last element
del a[1]  # Remove element at index 1

# Join, copy, and sort
b = [2, 4, 6]
a.extend(b)
copied_list = a.copy()
copied_list.sort()

# Loop through list and find max
print("Elements in list (break if 5):")
for elem in a:
    if elem == 5:
        print(elem)
        break
print("Largest number in list:", max(a))
