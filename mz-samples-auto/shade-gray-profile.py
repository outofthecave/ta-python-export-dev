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

    turtle.set_color(30.0)
    canvas.fillscreen_with_gray(0.0, 50.0, 0.0)
    turtle.set_pen_size(1.0)
    for i in range(int(100.0)):
        for i in range(int(100.0)):
            turtle.set_shade(float(turtle.get_x()) / tw.get_coord_scale())
            turtle.set_gray(float(turtle.get_y()) / tw.get_coord_scale())
            turtle.forward(turtle.get_pen_size())
            yield True
        turtle.set_pen_state(False)
        turtle.forward((-100.0))
        turtle.right(90.0)
        turtle.forward(turtle.get_pen_size())
        turtle.right((-90.0))
        turtle.set_pen_state(True)
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
