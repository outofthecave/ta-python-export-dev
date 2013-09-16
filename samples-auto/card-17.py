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
    turtle.set_color(0.0)
    BOX[u'sides'] = 8.0
    BOX[u'length'] = 200.0
    logo.icall(ACTION[u'action'])
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(6.0)):
        logo.icall(ACTION[u'polygon'])
        yield True
        BOX[u'sides'] = convert(BOX[u'sides'], TYPE_NUMBER) - 1.0
        BOX[u'length'] = convert(BOX[u'length'], TYPE_NUMBER) - 25.0
        turtle.set_color(turtle.get_color() + 15.0)
        yield True
    yield True
ACTION["action"] = action

def polygon():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.start_fill()
    for i in range(convert(BOX[u'sides'], TYPE_INT)):
        turtle.forward(convert(BOX[u'length'], TYPE_NUMBER))
        turtle.right(360.0 / convert(BOX[u'sides'], TYPE_NUMBER))
        yield True
    turtle.stop_fill()
    yield True
ACTION["polygon"] = polygon


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
