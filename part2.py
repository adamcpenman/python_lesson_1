def mult2(x):
    return x * 2


def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2


some_num = 12
y = mult2(some_num)
print(y)

some_nums = [1, 2, 3, 4]
print(some_nums)
mult2_list(some_nums)
print(some_nums)
