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

    BOX[u'my box_1'] = 0.0
    while (float(BOX[u'my box_1']) < 4.0):
        turtle.forward(100.0)
        turtle.right(90.0)
        BOX[u'my box_1'] = convert(BOX[u'my box_1'], TYPE_NUMBER) + 1.0
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


