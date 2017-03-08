#!/usr/bin/python

import time

def timeit(f):
    def new_f():
        print "Entering", f.__name__
        t1 = time.time()
        f()  ## Call the actual function
        t2 = time.time()
        print "Exited", f.__name__
        print "%s :%s secs"%(f.__name__, t2 - t1)
    return new_f

@timeit
def func1():
    time.sleep(1)
    print "inside func1()"

@timeit
def func2():
    time.sleep(2)
    print "inside func2()"

func1()
func2()

# --
