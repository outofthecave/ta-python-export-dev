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
    for i in range(int(10.0)):
        turtle.set_pen_size(int(round(uniform(int(10.0), int(100.0)), 0)))
        turtle.set_pen_state(False)
        turtle.set_xy(int(round(uniform(int(-200.0), int(200.0)), 0)), int(round(uniform(int(-150.0), int(150.0)), 0)))
        turtle.set_pen_state(True)
        turtle.set_shade(turtle.get_pen_size())
        turtle.forward(1.0)
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
