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

    if turtle.get_pen_state():
        turtle.forward(100.0)
    else:
        turtle.set_pen_state(True)
        turtle.forward((-100.0))
    turtle.set_pen_state(False)
    turtle.right(90.0)
    if turtle.get_pen_state():
        turtle.forward(100.0)
    else:
        turtle.set_pen_state(True)
        turtle.forward((-100.0))
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
