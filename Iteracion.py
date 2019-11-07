
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


for k in a:
    print(a[k])

for k,v in zip(b.keys(),b.values()):
    print(k,v)

for k in c:
    print((c[k]))

for k, v in zip(d.keys(),d.values()):
    print(k,v)

for k in e:
    print(e[k])

for k,v in zip(f.keys(),f.values()):
    print(k,v)

for k in g:
    print(g[k])

for k,v in zip(h.keys(),h.values()):
    print(k,v)

for k in i:
    print(i[k])

for k,v in zip(j.keys(),j.values()):
    print(j[k])
