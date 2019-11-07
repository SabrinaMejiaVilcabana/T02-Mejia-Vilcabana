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


del a["x"]
print(a)

del b["y"]
print(b)

del c["z"]
print(c)

del d["y"]
print(d)

del e["Sabrina"]
print(e)

del f["x"]
print(f)

del g["y"]
print(g)

del h["Hola"]
print(h)

del i["Cachorrito"]
print(i)

del j["m"]
print(j)
