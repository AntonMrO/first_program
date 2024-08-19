from random import randint
n = randint(3, 20)

result = ''
for i in range(1, n-1):
    for j in range(i+1, n-i+1):     #условие для исключения перебора чисел при сумме i+j больше n
        if n % (i+j) == 0 and j > i:
            result=result+str(i)+str(j)
        else:
            continue
print(f'{n} - {result}')
