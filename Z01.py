'''
Сайт для скачивания гита: https://git-scm.com/
Сайт гитхаба: https://github.com/
Основные команды для пользования гитом в командой строке:
1. git init (инициализирует репозиторий)
2. git status (отображает состояние репозитория и индексированных файлов)
3. git add . (добавляет все отслеживаемые файлы в индекс)
4. git commit –m ‘сообщение’ (сделать комит)
5. git push –u origin main (отправка изменений на удаленный сервер)
6. git remote add origin <ссылка> (привязка удаленного репозитория к локальному)
7. git pull (подгружает изменения с удаленного репозитория в локальный)
'''

# input -> "aabcd"
# output -> a-2 b-1 c-1 d-1

'''
# N**2
def strcounter(data):
	for sym in data:
		counter =0
		for sym2 in data:
			if sym==sym2:
				counter+=1
		print(sym, counter)
strcounter('aabcccd')
'''
# set - множество
# неупорядоченный тип данных, который хранит уникальные значения
'''
x=set()
v={1,1,2,3}
print(v)
r={}
print(type(r))
r={5}
print(type(r))

l=[1,1,2,3,1,2,5]
print(l)
# s=set(l)
# print(s)
# l=list(s)
l=list(set(l))
print(l)
'''
'''
# N*M
# N=len(data) M=set(data)
def strcounter(data):
	for sym in set(data):
		counter =0
		for sym2 in data:
			if sym==sym2:
				counter+=1
		print(sym, counter)
strcounter('aabcccd')
'''
'''
famaly ={}
print(famaly)
famaly['dad'] =1
print(famaly)
famaly['mom'] =1
print(famaly)
famaly['child']=famaly.get('child',0)+1
print(famaly)
'''
'''
#N
#N=len(data)
def strcounter(data):
	str_count={}
	for sym in data:
		str_count[sym] = str_count.get('child', 0) + 1
	print(str_count)
	for i, j in str_count.items():
		print(i,'-',j)

strcounter('aabcccd')
'''
'''
1 способ через терминал
- создать удаленный репозитарий
- выполнить команды в терминале

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Dasha577/111.git
git push -u origin main

'''
