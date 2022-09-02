my_list = [29, 41, 2, 4, 9, 13, 98, 131, 1, 9, 2, 4, 3]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)
