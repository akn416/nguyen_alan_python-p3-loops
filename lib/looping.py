#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i > 0):
        if i > 1: 
            print(i)
        else: 
            print(i)
            print("Happy New Year!")
        i-=1

def square_integers(int_list):
    new_list = list()
    for square in int_list:
        new_list.append(square * square)
    print(new_list)

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
