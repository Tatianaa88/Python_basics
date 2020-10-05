original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([original_list[i] for i in range(len(original_list)) if original_list[i] > original_list[i-1] and i != 0])
