class A:
    a = -1
    b = -1

    def __init__(self, _a, _b):
        self.a = _a
        self.b = _b

    def hello(self):
        print("This is a : " + str(self.a) + " this is b : " + str(self.b))

class Z(A):
    c = -1

    def __init__(self, _a, _b, _c):
        super().__init__(_a, _b)
        self.c = _c

    def greeting(self):
        print("This is a : " + str(self.a) + " this is b : " + str(self.b) + " this is c : " + str(self.c))

def main():
    print("startet")
    a1 = A("Python", 42)
    a1.hello()

    a2 = Z("Hello", 7, "There")
    a2.hello()
    a2.greeting()

main()
