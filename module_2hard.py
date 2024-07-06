def random_number(rand_num):
    parol_number = list()
    limit_num = (rand_num + 1) // 2
    for i in range(1, limit_num):
        j = i + 1
        while i + j <= rand_num:
            if rand_num % (i + j) == 0 and rand_num / (i + j) == 1:
                real_number = (i, j)
                parol_number.append(real_number)
            j += 1
    return parol_number

MP = True
while MP:
    first_number = int(input('Здравствуйтe! Введите первое число от 3 до 20: '))
    if first_number in range(3, 21):
        MP = False
    else:
        print('Вы ввели не коррктное число, повторите ввод!')
print('Для числа:', first_number, ',подходят числа:', random_number(first_number))
1
