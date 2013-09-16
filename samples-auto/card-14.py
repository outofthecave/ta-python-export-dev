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
    turtle.set_color(CONSTANTS['white'])
    turtle.set_pen_size(400.0)
    for i in range(int(200.0)):
        turtle.forward(1.0)
        turtle.forward((-1.0))
        turtle.set_shade(turtle.get_shade() - 0.5)
        turtle.set_pen_size(turtle.get_pen_size() - 2.0)
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
