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
    for i in range(int(350.0)):
        turtle.set_pen_size(turtle.get_heading() + 4.0)
        turtle.forward(1000.0)
        turtle.set_color(turtle.get_heading() / 3.0)
        BOX[u'my box'] = turtle.get_heading() / 2.0
        turtle.set_shade(100.0 - convert(BOX[u'my box'], TYPE_NUMBER))
        turtle.forward((-1000.0))
        turtle.right((-1.0))
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
