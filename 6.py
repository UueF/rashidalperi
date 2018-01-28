s=input()
t=s.lower()
k=t.find("коррупция")
if k!=-1:
	n=s[:k]+'*'*(len(s)-k)
else:
	n=s
print(n)