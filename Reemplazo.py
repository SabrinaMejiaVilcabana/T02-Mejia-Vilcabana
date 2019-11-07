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

a["x"] = "hola"
print(a)

b["y"] = "tamal"
print(b)

c["z"] = "Humita"
print(c)

d["y"] = "cafe"
print(d)

e["Sabrina"] ="Ethel"
print(e)

f["x"] = "Computadora"
print(f)

g["y"] = "mouse"
print(g)

h.update(a)
print(h)

i.update(b)
print(i)

j.update(c)
print(j)
