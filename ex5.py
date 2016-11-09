age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
	
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')