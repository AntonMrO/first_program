numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes =[]

for i in range(len(numbers)):
    is_prime = True
    if numbers[i] == 1:     #исключение 1, т.к. она не относится нги к простым ни к составным
        continue

    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:      #проверка остатка от деления на число, которое меньше проверяемого
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime == 0:                           #составление списка простых и не простых чисел в зависимости от флага is_Prime
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])

print('Простые числа:',primes)
print('Не простые (составные):',not_primes)
