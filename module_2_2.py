first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:        #сначала проверка наименее вероятного условия
    print('3')
elif first == second != third or first == third != second or second == third != first:
    print('2')
else:                   #ни одно условие выше не выполняется = нет одинаковых чисел
    print('0')