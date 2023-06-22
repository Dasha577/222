"""
На вход подается строка, все символы находятся в нижнем регистре и без пробелов.
Напишите функцию, которая будет возвращать True, если строка является палиндромом и False,
если строка палиндромом не является.
Примечание: палиндром — это строка, которая читается одинаково
как слева направо, так и справа налево
Пример входных данных 1: лепсспел
Пример выходных данных 1: True
Пример входных данных 2: helloworld
Пример выходных данных 2: False
ВАЖНО!
Отправьте решение данной задачи в ваш удаленный репозиторий, в качестве решение прикрепите ссылку на него.
В коммите кратко опишите, каким образом вы реализовали алгоритм проверки строки на палиндром.
В дальнейшем все домашнее задание вам необходимо будет сдавать при помощи git.
"""

def polindrom(t):
	for i in range(int(len(t)/2)):
		if t[i] != t[i*(-1)-1]:
			return False
	else: return True

print(polindrom(input('введите строку\n>> ')))
