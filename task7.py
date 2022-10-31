num_1 = int(input('введите число 1:\n'))
num_2 = int(input('введите число 2:\n'))
while num_1 != 0 and num_2 != 0:
    if num_1 > num_2:#Большее число делим на меньшее
        num_1 = num_1 % num_2
    else:
        num_2 = num_2 % num_1
print(num_1 + num_2)




"""
# то же но с вычитанием
num_1 = int(input('введите число 1:\n'))
num_2 = int(input('введите число 2:\n'))
while num_1 != num_2:
    if num_1 > num_2:
        num_1 = num_1 - num_2
    else:
        num_2 = num_2 - num_1
print(num_1)
"""