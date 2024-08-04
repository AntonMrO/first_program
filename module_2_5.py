# Задача "Матрица воплоти"
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        if n > 0:
            matrix.append([])   #добавляем пустую строку в список matrix

            for j in range(m):
                if m > 0:
                    matrix[i].append(value)         #добавляем значения value во вложенный список
                else:
                    matrix = []
                    break
        else:
            matrix = []
            break
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

result4 = get_matrix(int(input('Введите число строк: ')),int(input('Введите число столбцов: ')),input('Введите значение элемента: '))
print('Итоговая матрица: ')
print(result4)