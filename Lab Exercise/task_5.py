a = (1, 3, 5, 7, 4)
odd_sum = sum(x for x in a if x % 2 != 0)
extended_tuple = a + (2, 4, 6)
new_tuple = a[:2] + (200,) + a[2:]
modified_tuple = a[:-1]
sliced_tuple = a[-4:-1]

print("Sum of all odd numbers in tuple:", odd_sum)
print("Extended tuple:", extended_tuple)
print("Tuple after adding 200:", new_tuple)
print("Tuple after removing last element:", modified_tuple)
print("Sliced tuple [-4:-1]:", sliced_tuple)

print("Tuple elements (skipping 5):")
for num in a:
    if num == 5:
        continue
    print(num)
