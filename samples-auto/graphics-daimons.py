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

    canvas.fillscreen_with_gray(0.0, 0.0, 0.0)
    turtle.set_color(75.0)
    turtle.set_pen_size(7.0)
    logo.icall(ACTION[u'action 1'])
    yield True
ACTION["start"] = start

def action_1():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'my box 3'] = 100.0
    for i in range(int(70.0)):
        turtle.set_heading(0.0)
        turtle.set_shade(convert(BOX[u'my box 3'], TYPE_NUMBER))
        logo.icall(ACTION[u'action 2'])
        yield True
        turtle.set_heading(180.0)
        logo.icall(ACTION[u'action 2'])
        yield True
        BOX[u'my box 3'] = convert(BOX[u'my box 3'], TYPE_NUMBER) + 1.0
        yield True
    yield True
ACTION["action 1"] = action_1

def action_2():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'my box 1'] = 10.0
    BOX[u'my box 2'] = 200.0
    turtle.right(convert(BOX[u'my box 3'], TYPE_NUMBER))
    turtle.set_pen_state(False)
    turtle.set_xy(0.0, 0.0)
    turtle.set_pen_state(True)
    for i in range(int(40.0)):
        turtle.arc(convert(BOX[u'my box 2'], TYPE_NUMBER), convert(BOX[u'my box 1'], TYPE_NUMBER))
        turtle.right((-100.0))
        BOX[u'my box 1'] = convert(BOX[u'my box 1'], TYPE_NUMBER) + 10.0
        BOX[u'my box 2'] = convert(BOX[u'my box 2'], TYPE_NUMBER) - 10.0
        yield True
    yield True
ACTION["action 2"] = action_2


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
