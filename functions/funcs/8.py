#!/usr/bin/python


def main(arg1,arg2='empty'):   ## Dictionary gets distributed as args
    """ This is function help """
    print "Hello world ,arguments", arg1

arg = {
'arg2':{}
'arg1': 'I am here',
}

main(**arg)   ## Pack them in dictionary


# --
