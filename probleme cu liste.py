with open('input.txt','r')as f:
    lista1=f.readline()
    a=(lista1)
with open('lista1.txt','w') as f:
    f.write(str(a))
b=sorted(lista1)
with open('lista2.txt','w') as f:
     f.write(str(b))
c=sorted(lista1,reverse=True)
with open('lista3.txt','w') as f:
     f.write(str(c))
d=len(lista1)
with open('len.txt','w') as f:
     f.write(str(d))
e=max(lista1)
with open('max.txt','w') as f:
     f.write(str(e))
f=min(lista1)
with open('min.txt','w') as f:
     f.write(str(f))
g=lista1.extend([111])
print(g)
with open('list4.txt','w') as f:
     f.write(str(g))
lista1.remove(111)
lista1.insert(2,'222')
with open('lista5.txt','w') as f:
     f.write(str(lista1))