
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

a2 = a.pop("x")
print(a2)

b2 = b.pop("y")
print(b2)

c2 = c.pop("z")
print(c2)

d2 = d.pop("y")
print(d2)

e2 = e.popitem()
print(e2)

f2 = f.popitem()
print(f2)

g2 = g.popitem()
print(g2)

h2 = h.popitem()
print(h2)

i2 = i.pop("Cachorrito",16)
print(i2)
