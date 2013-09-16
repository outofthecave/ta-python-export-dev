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
    turtle.set_pen_size(10.0)
    for i in range(int(30.0)):
        turtle.set_pen_state(False)
        turtle.set_xy(int(round(uniform(int(-600.0), int(600.0)), 0)), int(round(uniform(int(-450.0), int(450.0)), 0)))
        turtle.set_pen_state(True)
        logo.icall(ACTION[u'bird'])
        yield True
    yield True
ACTION["start"] = start

def bird():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(720.0)):
        turtle.forward(200.0)
        turtle.set_shade(turtle.get_heading())
        turtle.set_color(float(turtle.get_x()) / tw.get_coord_scale() / 5.0)
        turtle.forward((-400.0))
        turtle.forward(int(round(uniform(int(190.0), int(210.0)), 0)))
        turtle.right((-1.0))
        yield True
    yield True
ACTION["bird"] = bird


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
