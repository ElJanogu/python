from random import random

def main():
    print("Programm gestartet")
    greeting()
    message("User")
    print(add(13, -6))
    print(rand())
    print("programm beendet")


def greeting():
    print("Hello There")


def message(message):
    print("Hello " + message)


def add(a, b):
    return a + b


def rand():
    return int(random() * 100)

main()
