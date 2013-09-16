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

    turtle.right(90.0)
    turtle.forward(100.0)
    turtle.right((-90.0))
    turtle.forward(float(turtle.get_x()) / tw.get_coord_scale())
    turtle.right((-90.0))
    turtle.forward(float(turtle.get_y()) / tw.get_coord_scale())
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
