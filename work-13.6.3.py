
def revers_number_and_sum(number_one, number_two):
    str_one = ''
    str_two = ''
    for i in reversed(str(number_one)):
        str_one += i
    for j in reversed(str(number_two)):
        str_two += j
    print('Первое число наоборот:', str_one)
    print('Второе число наоборот:', str_two)
    summ = int(str_one) + int(str_two)
    return summ

number_one = int(input('Введите первое число '))
number_two = int(input('Введите второе число '))
print('Сумма:', revers_number_and_sum(number_one, number_two))