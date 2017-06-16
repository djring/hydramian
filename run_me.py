# -*- coding: utf-8 -*-
import sys


def say_hello(name):
    print 'hello %s' % name

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print u'python run_me.py name'
        exit()
    say_hello(sys.argv[1])
