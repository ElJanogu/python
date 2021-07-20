class A:
    a = -1
    b = -1

    def __init__(self, _a, _b):
        self.a = _a
        self.b = _b

    def hello(self):
        return "This is a : " + str(self.a) + " this is b : " + str(self.b)

class Z(A):
    c = -1

    def __init__(self, _a, _b, _c):
        super().__init__(_a, _b)
        self.c = _c

    def greeting(self):
        return super(Z, self).hello() + " this is c : " + str(self.c)

def main():
    a1 = A("Python", 42)
    print(a1.hello())

    a2 = Z("Hello", 7, "There")
    print(a2.hello())
    print(a2.greeting())

main()
