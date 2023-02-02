"""
I/A:
A generált szám: 45
I/B:
A szám öttel és hárommal is osztható!
A.	Generálj egy véletlen egész  számot az [1, 50] zárt intervallumban!  (2p)
B.	A program írja ki a következők egyikét: (a mintának megfelelően – 1p):
•	Amennyiben a szám 5-tel osztható:
“A szám öttel osztható!”,
•	Amennyiben a szám 3-mal osztható:
“A szám hárommal  osztható!”,
•	Amennyiben a szám 5-tel és 3 – mal is osztható:
“A szám öttel és hárommal is osztható!”,

A három kiírás közül csak az egyik jelenjen meg a képernyőn!. (4p + 1p)
"""

import random

def veletlen_oszthatosag_vizsgalo():
    veletlen_szam = int(random.random() * 50 + 1)
    print(f"I/A: \nA generált szám: {veletlen_szam}")
    print("I/B:")
    if veletlen_szam % 3 == 0 and veletlen_szam % 5 == 0:
        print("A szám öttel és hárommal is osztható! ")
    elif veletlen_szam % 3 == 0:
        print("A szám hárommal osztható! ")
    elif veletlen_szam % 5 == 0:
        print("A szám öttel osztható! ")
    else:
        print("A szám sem öttel, sem hárommal nem osztható!")