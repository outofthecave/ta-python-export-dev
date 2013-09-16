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

    turtle.set_pen_size(3.0)
    BOX[u'size'] = 50.0
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], CONSTANTS['toppos'] - convert(BOX[u'size'], TYPE_NUMBER))
    turtle.set_pen_state(True)
    for i in range(int(float(CONSTANTS['height']) / convert(BOX[u'size'], TYPE_NUMBER))):
        turtle.set_pen_state(False)
        turtle.set_xy(CONSTANTS['leftpos'] - int(round(uniform(int(0.0), convert(BOX[u'size'], TYPE_INT)), 0)), float(turtle.get_y()) / tw.get_coord_scale())
        turtle.set_pen_state(True)
        for i in range(int(2.0 + float(CONSTANTS['width']) / convert(BOX[u'size'], TYPE_NUMBER) / 2.0)):
            turtle.set_color(CONSTANTS['blue'])
            logo.icall(ACTION[u'square'])
            yield True
            turtle.set_color(CONSTANTS['yellow'])
            logo.icall(ACTION[u'square'])
            yield True
        turtle.set_pen_state(False)
        turtle.set_xy(CONSTANTS['leftpos'], float(turtle.get_y()) / tw.get_coord_scale() - convert(BOX[u'size'], TYPE_NUMBER))
        turtle.set_pen_state(True)
        yield True
    yield True
ACTION["start"] = start

def square():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.start_fill()
    for i in range(int(4.0)):
        turtle.forward(convert(BOX[u'size'], TYPE_NUMBER))
        turtle.right(90.0)
        yield True
    turtle.stop_fill()
    turtle.set_gray(0.0)
    for i in range(int(4.0)):
        turtle.forward(convert(BOX[u'size'], TYPE_NUMBER))
        turtle.right(90.0)
        yield True
    turtle.set_pen_state(False)
    turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale() + convert(BOX[u'size'], TYPE_NUMBER), float(turtle.get_y()) / tw.get_coord_scale())
    turtle.set_pen_state(True)
    yield True
ACTION["square"] = square


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
