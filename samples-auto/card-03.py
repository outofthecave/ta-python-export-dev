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

    canvas.fillscreen_with_gray(60.0, 80.0, 100.0)
    BOX[u'side'] = 10.0
    for i in range(logo.int(10.0)):
        logo.icall(ACTION[u'square'])
        BOX[u'side'] = int(BOX[u'side']) + 20.0
        yield True
    yield True
ACTION["start"] = start

def square():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(logo.int(4.0)):
        turtle.forward(BOX[u'side'])
        turtle.right(90.0)
        yield True
    yield True
ACTION["square"] = square




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


