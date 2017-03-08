#!/usr/bin/python


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)  ## filter(func(x), list) To filter out values based on criteria
print map(lambda x: x * 2 + 10, foo)     ## map(func(x), list)To map each value 
print reduce(lambda x, y: x + y, foo)    ## reduct(func(x,y), list)To reduce the list 
