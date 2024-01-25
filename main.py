from microbit import *

while True:
    if button_a.is_pressed():
        print("hi")
        display.show("A")
    elif button_b.is_pressed():
        display.show("B")
    else:
        display.clear()
