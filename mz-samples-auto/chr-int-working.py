#!/usr/bin/env python

from math import sqrt
from random import uniform
from time import sleep

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[chr(int(97.0))] = 100.0
    for i in range(int(float(u'4.0e1'))):
        turtle.forward(convert(BOX[u'a'], TYPE_INT))
        turtle.right(int(CONSTANTS['purple']))
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


