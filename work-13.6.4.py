

def count_numbers(number):
    num_count = 0
    temp = number
    while temp > 0:
        num_count += 1
        temp = temp // 10
    return num_count

def change_number(number):
    last_digit = number % 10
    first_digit = number // 10 ** (count_numbers(number) - 1)
    between_digits = number % 10 ** (count_numbers(number) - 1) // 10
    new_number = last_digit * 10 ** (count_numbers(number) - 1) + between_digits * 10 + first_digit
    return new_number

def main():
    while True:
        print('')
        first_n = int(input("Введите первое число: "))
        second_n = int(input("\nВведите второе число: "))
        if count_numbers(first_n) < 3:
            print("В первом  числе меньше трёх цифр.")
            continue
        elif count_numbers(second_n) < 4:
            print("Во втором числе меньше четырёх цифр.")
            continue
        else:
            count_numbers(first_n)
            print('Изменённое первое число:', change_number(first_n))
            count_numbers(second_n)
            print('Изменённое первое число:', change_number(second_n))
            print('\nСумма чисел:', change_number(first_n) + change_number(second_n))

main()


