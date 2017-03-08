#!/usr/bin/python

def main():
    x = 3  ## Local variable
    f()

def f():
    print(x)  # error: f does not know about the x defined in main

main()
