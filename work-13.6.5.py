
start = float(input('Введите начальную амплитуду маятника '))
stop = float(input('Введите конечную амплитуду маятника '))
count = 0
if start < stop or stop < 0 or start < 0:
    print('Ошибка ввода')
else:
    while start > stop:
        count += 1
        start -= (start * 0.084)
    print(f"\nМаятник считается остановившимся через {count} колебаний\n")

