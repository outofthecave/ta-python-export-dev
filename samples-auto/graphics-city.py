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

    tw.clear_plugins()
    logo.stop_playing_media()
    logo.reset_scale()
    logo.reset_timer()
    logo.clear_value_blocks()
    logo.reset_internals()
    canvas.clearscreen()
    turtles.reset_turtles()
    canvas.fillscreen(60.0, 0.0)
    BOX[u'my box 1'] = int(round(uniform(int(75.0), int(125.0)), 0))
    BOX[u'top'] = CONSTANTS['toppos'] - 100.0
    for i in range(int(100.0)):
        turtle.set_color(int(round(uniform(int(0.0), int(10.0)), 0)))
        turtle.set_shade(CONSTANTS['toppos'] - convert(BOX[u'top'], TYPE_NUMBER) / 8.0)
        turtle.set_pen_state(False)
        turtle.set_xy(int(round(uniform(int(CONSTANTS['leftpos'] - 50.0), CONSTANTS['rightpos']), 0)), convert(BOX[u'top'], TYPE_NUMBER))
        turtle.set_pen_state(True)
        logo.icall(ACTION[u'building'])
        yield True
        logo.icall(ACTION[u'roof'])
        yield True
        BOX[u'top'] = convert(BOX[u'top'], TYPE_NUMBER) - 3.0
        yield True
    yield True
ACTION["start"] = start

def roof():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_heading(45.0)
    turtle.start_fill()
    for i in range(int(4.0)):
        turtle.forward(convert(BOX[u'my box 1'], TYPE_NUMBER))
        turtle.right(90.0)
        yield True
    turtle.stop_fill()
    turtle.set_shade(turtle.get_shade() + 50.0)
    for i in range(int(4.0)):
        turtle.forward(convert(BOX[u'my box 1'], TYPE_NUMBER))
        turtle.right(90.0)
        yield True
    turtle.set_heading(135.0)
    turtle.forward(convert(BOX[u'my box 1'], TYPE_NUMBER))
    turtle.set_heading(180.0)
    turtle.forward(float(turtle.get_y()) / tw.get_coord_scale() - CONSTANTS['bottompos'])
    turtle.set_shade(turtle.get_shade() - 50.0)
    yield True
ACTION["roof"] = roof

def building():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_heading(180.0)
    BOX[u'my box 2'] = float(turtle.get_y()) / tw.get_coord_scale() - CONSTANTS['bottompos']
    turtle.start_fill()
    for i in range(int(2.0)):
        turtle.forward(convert(BOX[u'my box 2'], TYPE_NUMBER))
        turtle.right((-90.0))
        turtle.forward(convert(BOX[u'my box 1'], TYPE_NUMBER) * sqrt(2.0))
        turtle.right((-90.0))
        yield True
    turtle.stop_fill()
    turtle.set_shade(turtle.get_shade() + 50.0)
    for i in range(int(2.0)):
        turtle.forward(convert(BOX[u'my box 2'], TYPE_NUMBER))
        turtle.right((-90.0))
        turtle.forward(convert(BOX[u'my box 1'], TYPE_NUMBER) * sqrt(2.0))
        turtle.right((-90.0))
        yield True
    turtle.set_shade(turtle.get_shade() - 50.0)
    yield True
ACTION["building"] = building


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
