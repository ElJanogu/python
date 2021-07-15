
a = 5

if a == 5:
    print("a == 5")
elif a < 5:
    print("a < 5")
else:
    print("a > 5")

b = 22

if b > 17: print("b > 17")

print("ja") if b < 13 else print("nein")

print(">") if b > 99 else print("=") if b == 99 else print("<")

c = 4
d = 56

if c < 17 and d > 4:
    print("some source code")

if c < 17 or d > 4:
    print("some source code")

e = 99

if e <= 100:
    pass

f = 1
while f < 6:
    print(f)
    f += 1
else:
    print("i ist nicht mehr kleiner als 6")

g = "Hello there"

for g_ in g:
    print(g_)
    # pass
else:
    print("fertig")

