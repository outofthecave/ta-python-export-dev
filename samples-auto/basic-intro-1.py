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
    BOX[u'box 2'] = 1.0
    for i in range(int(2.0)):
        logo.icall(ACTION[u'action'])
        yield True
        BOX[u'box 2'] = convert(BOX[u'box 2'], TYPE_NUMBER) + 1.0
        yield True
    yield True
ACTION["start"] = start

def _1_0():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(convert(BOX[u'box 1'], TYPE_INT)):
        turtle.forward(100.0)
        turtle.right(360.0 / convert(BOX[u'box 1'], TYPE_NUMBER))
        yield True
    yield True
ACTION["1.0"] = _1_0

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'box 1'] = 12.0
    for i in range(int(10.0)):
        turtle.set_color(CONSTANTS['red'])
        turtle.set_gray(300.0 / convert(BOX[u'box 1'], TYPE_NUMBER))
        turtle.start_fill()
        logo.icall(ACTION[convert(BOX[u'box 2'], TYPE_STRING)])
        yield True
        turtle.stop_fill()
        turtle.set_color(CONSTANTS['orange'])
        logo.icall(ACTION[convert(BOX[u'box 2'], TYPE_STRING)])
        yield True
        BOX[u'box 1'] = convert(BOX[u'box 1'], TYPE_NUMBER) - 1.0
        yield True
    yield True
ACTION["action"] = action

def _2_0():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(convert(BOX[u'box 1'], TYPE_INT)):
        turtle.forward(100.0)
        turtle.right((-360.0 / convert(BOX[u'box 1'], TYPE_NUMBER)))
        yield True
    yield True
ACTION["2.0"] = _2_0


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
