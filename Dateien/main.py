"""
f = open(..., x) -> create the file
f = open(..., w) -> create the file if not exist

a = append
r = read (default)

je nur einen der testfaelle nutzen
sonst funktioniert es nicht richtig, danke ^^
"""

f = open("test.txt", "r")
print(f.read())

#print(f.read(2))

#print(f.readline())

#for line in f:
#    print(line)

f.close()

#f = open("test.txt", "w")
#f.write("This is the new text")

#f.close()