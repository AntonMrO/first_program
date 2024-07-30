my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, 6, 5]
dl = 0
while dl < len(my_list):        #условие по сравнению значения переменной с длиной  списка
    if my_list[dl] > 0:
        print(my_list[dl])
        dl = dl + 1
    elif my_list[dl] == 0:
        dl = dl + 1
    else:
        break