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

a.setdefault("hola","bola")
print(a)

b.setdefault("uno","dos")
print(b)

c.setdefault("futbol","basquet")
print(c)

d.setdefault(1,"impresora")
print(d)

e.setdefault("uva","mesa")
print(e)

f.setdefault("vaso","agua")
print(f)

g.setdefault("cable","electrico")
print(g)

h.setdefault("usb","conector")
print(h)

i.setdefault("celular","serie")
print(i)

j.setdefault("netflix","cable")
print(j)
