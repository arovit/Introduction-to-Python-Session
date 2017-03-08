#!/usr/bin/python


def main(*rarg):  # Receive them in a packed tuple
    """ This is function help """
    print "Hello world ,arguments",rarg

arg = [1,2,3,4,5]
main(*arg)        # Pack them in a tuple 
