def polindrom(t):
	return True if t==t[::-1] else False

print(polindrom(input('введите строку\n>> ')))
