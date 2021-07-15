"""
Disclaimer :
nicht beide beispiele auf einmal verwenden
immer mindestens eines auskommentieren
"""

from pynput import keyboard
"""
COMBINATIONS = [
    {keyboard.KeyCode(char="q")},
    {keyboard.KeyCode(char="Q")}
]

number = -1

current = set()

def execute():
    print("Detected key")
    global number
    number = number + 1
    print(str(number))

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        print("release")


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
"""

while(True):
    e = input("Enter Something")
    print("Message : " + e)
