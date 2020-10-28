#scitanie test

#importovanie knižníc

from time import *
import threading
from os import system
import random

#deklarovanie premenných
x = 0
skore = 0
max_skore = 0

#vytvorenie funkcie

def countdown():
    global my_timer

    my_timer = 5
    for x in range(5):
        my_timer = my_timer-1
        sleep(1)
    system('cls')
    print('Čas vypršal')
    print('Skore:', skore)

#thread


#hlavny program

countdown_thread = threading.Thread(target = countdown)
print('''Test z Matematiky
Sčítanie
Odčítanie
Nasobenie
Delenie''')
mod = input('')
system('cls')
if mod == 'scitanie':
    print('''Test z šcitania 
Akú vyber si obťiažnosť:
Easy
Medium
Hard''')
    obtiaznost = input('')
    system('cls')

    countdown_thread.start()

    if obtiaznost == 'easy':
        while my_timer > 0:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print(a, '+', b, '=')
            v = a + b
            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'medium':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            print(a, '+', b, '=')
            v = a + b

            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'hard':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            print(a, '+', b, '=')
            v = a + b

            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    else:
        print('Neplatna volba')
if mod == 'odcitanie':
    print('''Test z šcitania 
Akú vyber si obťiažnosť:
Easy
Medium
Hard''')
    obtiaznost = input('')
    system('cls')

    countdown_thread.start()

    if obtiaznost == 'easy':
        while my_timer > 0:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print(a, '-', b, '=')
            v = a - b
            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'medium':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            print(a, '-', b, '=')
            v = a - b

            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'hard':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            print(a, '-', b, '=')
            v = a - b

            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    else:
        print('Neplatna volba')
if mod == 'nasobenie':
    print('''Test z šcitania 
Akú vyber si obťiažnosť:
Easy
Medium
Hard''')
    obtiaznost = input('')
    system('cls')

    countdown_thread.start()

    if obtiaznost == 'easy':
        while my_timer > 0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            print(a, '*', b, '=')
            v = a * b
            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'medium':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print(a, '*', b, '=')
            v = a * b

            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'hard':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 30)
            b = random.randint(1, 30)
            print(a, '*', b, '=')
            v = a * b

            cislo = int(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    else:
        print('Neplatna volba')
if mod == 'delenie':
    print('''Test z šcitania 
Akú vyber si obťiažnosť:
Easy
Medium
Hard''')
    obtiaznost = input('')
    system('cls')

    countdown_thread.start()

    if obtiaznost == 'easy':
        while my_timer > 0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            print(a, '/', b, '=')
            v = a / b
            cislo = float(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'medium':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print(a, '/', b, '=')
            v = a / b

            cislo = float(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    elif obtiaznost == 'hard':
        while my_timer > 0:
            max_skore = max_skore + 1
            a = random.randint(1, 30)
            b = random.randint(1, 30)
            print(a, '/', b, '=')
            v = a / b

            cislo = float(input(''))
            if cislo == v:
                skore = skore + 1
                print('Správne')
                sleep(1)
                system('cls')
            else:
                print('Nesprávne')
                sleep(1)
                system('cls')
            if my_timer == 0:
                break
    else:
        print('Neplatna volba')
else:
    print('Neplatna volba')
#skore
input()
