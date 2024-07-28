    #домашнее задание для модуля 1
grades = [[5, 3 ,3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]     #спискок оценок
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}     #исходные данные - список учеников

students = list(students)     #перевод списка студентов в упорядоченный список и сортировка по алфавиту
stud = students.sort()  

grades = [sum(grades[0])/len(grades[0]),    #расчет средней оценки каждого студента и обновление оценок в списке оценок
          sum(grades[1])/len(grades[1]),
          sum(grades[2])/len(grades[2]),
          sum(grades[3])/len(grades[3]),
          sum(grades[4])/len(grades[4])]

dnev_stud = dict(zip(students, grades))     #составление словаря со списокм учеников и их средней оценки

#dnev_stud = {students[0] : grades[0],      #второй вариант без функции zip - составление словаря со списокм учеников и их средней оценки
#             students[1] : grades[1],
#             students[2] : grades[2],
#             students[3] : grades[3],
#             students[4] : grades[4]}

print(dnev_stud)                # вывод на экран списка