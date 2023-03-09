path = [1, 2, 3]
path_copy1 = path[:]
path_copy2 = list(path)

path.append(4)

print(path)        # Output: [1, 2, 3, 4]
print(path_copy1)  # Output: [1, 2, 3]
print(path_copy2)  # Output: [1, 2, 3]

