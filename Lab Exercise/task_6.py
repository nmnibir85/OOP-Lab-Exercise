# Define the sets a and b
a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

# Print the sets and their types
print("Set a:", a)
print("Type of a:", type(a))
print("Set b:", b)
print("Type of b:", type(b))

# Print the length of the sets
print("Length of set a:", len(a))
print("Length of set b:", len(b))

# Add a new element 10 to set a
a.add(10)

# Remove 8 from set a
a.remove(8)

# Perform union, intersection, difference, symmetric difference, and subset operations
union_set = a.union(b)
intersection_set = a.intersection(b)
difference_set = a.difference(b)
symmetric_difference_set = a.symmetric_difference(b)
is_subset = a.issubset(b)

print("Union of a and b:", union_set)
print("Intersection of a and b:", intersection_set)
print("Difference of a and b:", difference_set)
print("Symmetric difference of a and b:", symmetric_difference_set)
print("Is set a a subset of set b?", is_subset)

# Join a new list [2, 3, 4] with set a
new_list = [2, 3, 4]
set_a_joined = a.union(set(new_list))

print("Set a after joining the new list:", set_a_joined)
