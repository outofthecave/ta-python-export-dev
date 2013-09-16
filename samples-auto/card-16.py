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
    turtle.set_pen_size(25.0)
    logo.icall(ACTION[u'action'])
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(40.0)):
        turtle.set_pen_state(False)
        turtle.set_xy(50.0 * int(round(uniform(int(-4.0), int(4.0)), 0)), 50.0 * int(round(uniform(int(-3.0), int(3.0)), 0)))
        turtle.set_pen_state(True)
        turtle.forward(1.0)
        yield True
    yield True
ACTION["action"] = action


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
