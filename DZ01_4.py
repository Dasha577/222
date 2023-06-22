def polindrom(t):
	for i in range(int(len(t)/2)):
		if t[i] != t[i*(-1)-1]:	return False
	else: return True

print(polindrom(input('введите строку\n>> ')))
