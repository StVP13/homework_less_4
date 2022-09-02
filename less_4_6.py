from itertools import count, cycle

my_count = count(10)
my_cycle = cycle('OMG')

for _ in range(20):
    print('(my_count, my_cycle) = ({},{}, wow, amazing)'.format(next(my_count), next(my_cycle)))
