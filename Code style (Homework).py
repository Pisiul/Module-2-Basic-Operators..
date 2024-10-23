
# ************************************************* Домашнее задание ************************************************* #
# ********************************* ( "Цели и задачи. Поток выполнения программы" ) ********************************** #


#           Цель: применить навыки создания цикла while, а так же применения операторов break и continue.
#
# Задача №1: "Нули ничто, отрицание недопустимо!":
#
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не
# закончится список (выход за границу).
#
# Пункты задачи:
#
#     Запишите исходный список в переменную my_list.
#     Напишите цикл while с соответствующими задаче условиями.
#     Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.
#
#     Чтобы перебрать список вам понадобиться обращение по индексу, запишите в отдельную
#     переменную начальное значение - 0.
#     Чтобы не выйти за границу списка, в условии цикла while рекомендуется сравнивать текущий индекс и длину списка
#     (функция len()).
#     Оператор continue - возвращает вас к условию цикла, игнорируя код после себя, break - прерывает цикл.
#     0 - не отрицательное и не положительное число.
#
# -------------------------------------------------------------------------------------------------------------------- #

# Ответ №1:

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходный список
print(my_list)
index = 0  # - индекс начинается с нуля и используем как обращение к списку.
elem = my_list[index]  # - создаем переменную elem которая является нашим списком.
while elem >= 0:  # - ставим значение больше или равно нулю для работы цикла.
    elem = my_list[index]
    index += 1  # - извлекаем индекс из списка и прибавляем единицу для перечисления элементов.
    if elem < 0:  # - если у нас элемент меньше нуля, то мы завершаем наш цикл/
        break
    elif elem == 0:  # - Если элемент равен нулю то просто пропускаем.
        index = -5  # - пересчет элементов в обратном направлении.
        continue
    print(elem)
# -------------------------------------------------------------------------------------------------------------------- #
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe "D:\Программы\ProjectPyton\Module 2
# Basic Operators\Code style (Homework).py"
# [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# 42
# 69
# 322
# 13
# 9
# 8
# 7
#
# Process finished with exit code 0
# -------------------------------------------------------------------------------------------------------------------- #
