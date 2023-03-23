
def maximum_of_two(number_one, number_two):
    return max(number_one, number_two)

def maximum_of_three(number_one, number_two, number_three):
    return max(maximum_of_two(number_one, number_two), number_three)

number_one = int(input('Введите первое число '))
number_two = int(input('Введите второе число '))
number_three = int(input('Введите третье число '))

print('Максимальное число из', number_one, number_two, number_three, 'будет', maximum_of_three(number_one, number_two, number_three))


