from functools import reduce


def another_list(el_1, el_2):
    return el_1 * el_2


wonderful_list = [el for el in range(100, 1001, 3)]
print(f'СПИСОК\n{wonderful_list}\nМАГИЯ\n{reduce(another_list, wonderful_list)}')
