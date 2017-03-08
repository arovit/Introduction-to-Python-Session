#!/usr/bin/python


def main(*args):  # Receive them in a packed tuple
    """ This is function help """
    i = args[0]
    print "Hello world ,arguments %s"%str(args)

arg1 = "inp1"
arg2 = "inp2"
arg3 = "inp3"
arg4 = "inp4"
arg5 = "inp5"
main(arg1,arg2,arg3,arg4,arg5)
