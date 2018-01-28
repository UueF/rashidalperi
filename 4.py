l=0
s=''
for i in range(0,3):
	t=input()
	if l<len(t):
		l=len(t)
		s=t

print('Самое первое имя максимальной длины:',s)