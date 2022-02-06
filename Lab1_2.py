#Подключение библиотеки с готовыми функциями сортировки
import sorting
import random
fl = False
while not fl:
		print('1 - Ввод с клавиатуры, 2 - генерация случайных чисел')
		#Ввод выбранного оператора:
		choose_input = int(input())
		#Проверка на выбранный вариант:
		if choose_input == 1:
			change_list = []
			#Формирование списка через клавиатуру
			change_list = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
			print(change_list)
			#Вывод отсортированного массива
			res = sorting.selection(change_list)
			print('Сортировка выбором   : ', res)
		if choose_input == 2:
			change_list = []
			print('Введите размер списка:')
			#Ввод размера случайного списка
			ran_num = int(input())
			for i in range(0,int(ran_num)):
				n = random.randint(1,30)
				change_list.append(n)
			print(change_list)
			#Вывод отсортированного массива
			res = sorting.selection(change_list)
			print('Сортировка выбором   : ', res)
			'''Тест редактирования3'''