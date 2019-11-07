

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

print("y" in a)
print("y" in b)
print("z" in c)
print("2" in d)
print("Sabrina" in e)
print("x" not in f)
print("z" not in g)
print("Hola" not in h)
print("Cachorrita" in i)
print("m" not in j)
