path = [1, 2, [3, 4]]
path_copy = path[:]
path[2].append(5)

print(path)       # Output: [1, 2, [3, 4, 5]]
print(path_copy)  # Output: [1, 2, [3, 4]]
