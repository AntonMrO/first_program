    #работа со словарем
my_dict = {'Studia_Moscow' : [1,12000000], 'Odnokomn_Moscow' : [1, 18000000], 'Dvuhkomn_Saint-Peterburg' : [2, 21000000]}   #список из кол-ва комнат и цены квартир в разных города
print('Price houses:',my_dict)
print('Existing value:',my_dict['Odnokomn_Moscow'])        #вывод одного элемента
print('Not Existing value:',my_dict.get('Dvuhkomn_Moscow'))      #вывод отсутствующего элемента без выдачи ошибки
my_dict.update({'Odnokomn_Kazan' : [1, 6000000],
                'Dvuhkomn_Kazan' : [2, 11000000]})        #добавляем два новых элемента в словарь
l = my_dict.pop('Dvuhkomn_Saint-Peterburg')        #извлечение элемента и значения, запись значения в переменную
print('Deleted value:',l)
print('Modify price houses:',my_dict)
print('-----')

    #работы с множеством
my_set = {2000, 2001, 2002, 1986, 1961, 1998, 'Olimpic Games', 'Organic', True, 18.96, 1961, 'Organic', 1986, 2002, True}
print('My Set:',my_set)
my_set.add(1991)        #добавить 1 элемент
my_set.add('Rally')     #добавить еще 1 элемент
my_set.discard(2001)    #удалить элемент
print('My New Set:',my_set)