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

a["x"] = "oso"
print(a)

b["y"] = "panda"
print(b)

c["z"] = "hormiga"
print(c)

d["y"] = "cucaracha"
print(d)

e["Sabrina"] ="abeja"
print(e)

f["x"] = "reina"
print(f)

g["y"] = "raton"
print(g)

h["Hola"] = "sapo"
print(h)

i["Cachorrito"] = "rana"
print(i)

j["m"] = "zorro"
print(j)
