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

    BOX[u'color 1'] = 40.0
    BOX[u'color 2'] = 10.0
    BOX[u'color 3'] = 90.0
    canvas.fillscreen(convert(BOX[u'color 1'], TYPE_NUMBER), 50.0)
    BOX[u'box 1'] = CONSTANTS['width'] / 12.0
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], CONSTANTS['toppos'])
    turtle.set_pen_state(True)
    turtle.set_pen_size(10.0)
    turtle.set_heading(90.0)
    BOX[u'box 2'] = 0.0
    logo.icall(ACTION[u'action'])
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(float(CONSTANTS['height'] / 10.0))):
        BOX[u'box 2'] = 1.0 - convert(BOX[u'box 2'], TYPE_NUMBER)
        logo.icall(ACTION[u'action_2'])
        yield True
        turtle.set_pen_state(False)
        turtle.set_xy(CONSTANTS['leftpos'], float(turtle.get_y()) / tw.get_coord_scale() + -10.0)
        turtle.set_pen_state(True)
        yield True
    yield True
ACTION["action"] = action

def action_2():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(3.0)):
        if (convert(BOX[u'box 2'], TYPE_NUMBER) == 0.0):
            logo.icall(ACTION[u'stripe b'])
            yield True
        else:
            logo.icall(ACTION[u'stripe a'])
            yield True
        yield True
    yield True
ACTION["action_2"] = action_2

def stripe_b():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    turtle.set_pen_state(True)
    turtle.set_color(convert(BOX[u'color 2'], TYPE_NUMBER))
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    turtle.set_pen_state(False)
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    turtle.set_pen_state(True)
    turtle.set_color(convert(BOX[u'color 3'], TYPE_NUMBER))
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    yield True
ACTION["stripe b"] = stripe_b

def stripe_a():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_color(convert(BOX[u'color 2'], TYPE_NUMBER))
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    turtle.set_color(convert(BOX[u'color 3'], TYPE_NUMBER))
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    turtle.set_color(convert(BOX[u'color 2'], TYPE_NUMBER))
    turtle.forward(convert(BOX[u'box 1'], TYPE_NUMBER))
    yield True
ACTION["stripe a"] = stripe_a


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
