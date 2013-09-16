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
    turtle.set_pen_state(False)
    turtle.set_xy(-100.0, 200.0)
    turtle.set_pen_state(True)
    turtle.set_pen_size(30.0)
    logo.icall(ACTION[u'action'])
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(5.0)):
        logo.icall(ACTION[u'line'])
        yield True
        turtle.set_pen_state(False)
        turtle.set_xy(-100.0, float(turtle.get_y()) / tw.get_coord_scale() - 60.0)
        turtle.set_pen_state(True)
        yield True
    yield True
ACTION["action"] = action

def line():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(5.0)):
        turtle.forward(1.0)
        turtle.forward((-1.0))
        turtle.set_pen_state(False)
        turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale() + 60.0, float(turtle.get_y()) / tw.get_coord_scale())
        turtle.set_pen_state(True)
        yield True
    yield True
ACTION["line"] = line


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
