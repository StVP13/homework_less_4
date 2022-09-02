from random import randint

my_homework_l4_2nd_list = [randint(-25, 25) for _ in range(20)]
mystery_list = [el for el in my_homework_l4_2nd_list if my_homework_l4_2nd_list.count(el) == 1]
print(f"исходный список\n{my_homework_l4_2nd_list}\nнеповторимый список\n{mystery_list}")
