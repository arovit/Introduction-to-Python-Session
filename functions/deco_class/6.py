#!/usr/bin/python

def generate_ints(N):
    for i in range(N):
        yield i



gen = generate_ints(10)

print gen.next()
print gen.next()    
