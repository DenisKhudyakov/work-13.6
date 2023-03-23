
def teacher_program(number):
    count = 0
    while number > 10:
        number /= 10
        count += 1
    while number < 1:
        number *= 10
        number = round(number, 3)
        count -= 1
    print(f"Формат плавающей точки: x = {number} * 10 ** {count}")

number = float(input('Введите число '))
teacher_program(number)

