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

    canvas.fillscreen(10.0, 30.0)
    turtle.set_shade(85.0)
    turtle.set_pen_state(False)
    turtle.set_xy(-590.0, -450.0)
    turtle.set_pen_state(True)
    turtle.set_pen_size(3.0)
    for i in range(int(6.0)):
        turtle.set_heading(0.0)
        logo.icall(ACTION[u'action'])
        yield True
        turtle.set_pen_state(False)
        turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale() + 200.0, float(turtle.get_y()) / tw.get_coord_scale())
        turtle.set_pen_state(True)
        yield True
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(400.0)):
        BOX[u'my box 1'] = turtle.get_heading() / 2.0
        BOX[u'my box 2'] = convert(BOX[u'my box 1'], TYPE_NUMBER) + 5.0
        turtle.set_color(int(round(uniform(convert(BOX[u'my box 1'], TYPE_INT), convert(BOX[u'my box 2'], TYPE_INT)), 0)))
        turtle.arc(-40.0, 3000.0)
        turtle.arc(-40.0, -3000.0)
        turtle.right(0.1)
        yield True
    yield True
ACTION["action"] = action


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
