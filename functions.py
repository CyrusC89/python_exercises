#!/usr/bin/env python
# number = raw_input()

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def main():
    first_number = int(raw_input())
    operator = raw_input()
    second_number = int(raw_input())
    
    if operator == "+":
        print addition(first_number, second_number)
    elif operator == "-":
        print subtraction(first_number, second_number)

main()

