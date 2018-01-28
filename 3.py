s='Век живи - век учись'
d=''
for i in s:
	if i=='е':
		d=d+'и'
	elif i=='и':
		d=d+'е'
	else:
		d=d+i

print(d)

s=s.replace('и', 'e') #буква е английская
s=s.replace('е','и')
print(s)