    #homework5 kortezh and list
    #1
immutable_var = (17, 71,"goal", True, 4.54, 'house')
print(immutable_var)
    #2
immutable_var[1] = 72       #кортеж не является изменяемым списком, элементы менять не возможно. Выдает ошибку
    #3
mutable_list = [88, 99, 111, False, "element_1", "element_2", 35.4, 13.23]
print(mutable_list)
mutable_list[0] = 77        #замена по 1 элементу в списке
mutable_list[3] = True
mutable_list[-2] = "element_3"
print(mutable_list)

mutable_list = [66, 99, 333, False, "element_1", "element_2", "element_3", "element_4"] #замена списка
print(mutable_list[0:4])