array = [1, 2, 4, 9, 1]

are_all_int = all(isinstance(x, int) for x in array)

print(are_all_int)