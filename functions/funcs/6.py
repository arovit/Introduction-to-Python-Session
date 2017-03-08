#!/usr/bin/python


def main(arg1,arg2,arg3,arg4,arg5):  
    """ This is function help """
    print "Hello world ,arguments",arg1,arg2,arg3,arg4,arg5

arg = [1,2,3,4,5]
main(*arg)   ## To pack all the arguement 
