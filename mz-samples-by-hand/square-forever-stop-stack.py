#!/usr/bin/env python

from math import sqrt
from random import uniform

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
    while True:
        if (int(BOX[u'my box_1']) > 3.0):
            break
        turtle.forward(100.0)
        turtle.right(90.0)
        BOX[u'my box_1'] = int(BOX[u'my box_1']) + 1.0
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


