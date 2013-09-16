#!/usr/bin/env python

from time import *
from random import uniform
from math import *

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}


def start():
    tw.start_plugins()
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    canvas.fillscreen_with_gray(60.0, 80.0, 100.0)
    BOX[u'side'] = 10.0
    for i in range(int(10.0)):
        logo.icall(ACTION[u'square'])
        yield True
        BOX[u'side'] = convert(BOX[u'side'], TYPE_NUMBER) + 20.0
        yield True
    yield True
ACTION["start"] = start

def square():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(4.0)):
        turtle.forward(convert(BOX[u'side'], TYPE_NUMBER))
        turtle.right(90.0)
        yield True
    yield True
ACTION["square"] = square


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
