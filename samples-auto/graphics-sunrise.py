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

    canvas.fillscreen(0.0, 0.0)
    turtle.set_pen_size(6.0)
    for i in range(int(300.0)):
        BOX[u'my box 1'] = 15.0
        BOX[u'my box 2'] = 20.0
        logo.icall(ACTION[u'sunrise'])
        yield True
        BOX[u'my box 1'] = 0.0
        BOX[u'my box 2'] = 10.0
        logo.icall(ACTION[u'sunrise'])
        yield True
    yield True
ACTION["start"] = start

def sunrise():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.set_xy(0.0, 0.0)
    turtle.set_pen_state(True)
    turtle.set_heading(int(round(uniform(int(0.0), int(360.0)), 0)))
    for i in range(int(20.0)):
        turtle.set_color(int(round(uniform(convert(BOX[u'my box 1'], TYPE_INT), convert(BOX[u'my box 2'], TYPE_INT)), 0)))
        turtle.forward(int(round(uniform(int(10.0), int(30.0)), 0)))
        turtle.right(int(round(uniform(int(30.0), int(40.0)), 0)))
        turtle.set_color(int(round(uniform(convert(BOX[u'my box 1'], TYPE_INT), convert(BOX[u'my box 2'], TYPE_INT)), 0)))
        turtle.forward(int(round(uniform(int(10.0), int(30.0)), 0)))
        turtle.right((-int(round(uniform(int(30.0), int(40.0)), 0))))
        yield True
    yield True
ACTION["sunrise"] = sunrise


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
