a = dict(x=1,y=4)
b = dict(y=2)
c = dict(z=3)
d = {"x":1,"y":"2"}
e = dict({"Sabrina":"72086616"})
f = dict(zip(a,b))
g = dict(zip(b,c))
h = dict({"Hola":"Bienvenido"})
i = dict({"Cachorrito":"Cachorrita"})
j = dict(m=4)


lista = list(a)
tupla = tuple(b)
lista3 = list(c)
lista_v = list(d.values())
tupla_v = tuple(e.values())
tupla3 = tuple(f)
lista2 = list(g)
tupla2 = tuple(h)
lista_v3 = list(i.values())
lista_v2 = list(j.values())

print(lista)
print(tupla)
print(lista3)
print(lista_v)
print(tupla_v)
print(tupla3)
print(lista2)
print(tupla2)
print(lista_v3)
print(lista_v2)
