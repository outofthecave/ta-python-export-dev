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
    BOX[u'side'] = 0.0
    BOX[u'pen'] = 0.0
    logo.icall(ACTION[u'action'])
    yield True
ACTION["start"] = start

def spinner():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(10.0)):
        logo.icall(ACTION[u'square'])
        yield True
        turtle.right(36.0)
        yield True
    yield True
ACTION["spinner"] = spinner

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

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(100.0)):
        turtle.set_color(convert(BOX[u'pen'], TYPE_NUMBER) / 3.0)
        turtle.set_shade(100.0 - convert(BOX[u'pen'], TYPE_NUMBER))
        logo.icall(ACTION[u'spinner'])
        yield True
        BOX[u'pen'] = convert(BOX[u'pen'], TYPE_NUMBER) + 1.0
        BOX[u'side'] = convert(BOX[u'side'], TYPE_NUMBER) + 2.0
        yield True
    yield True
ACTION["action"] = action


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
