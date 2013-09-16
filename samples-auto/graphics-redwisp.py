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
    turtle.set_pen_size(15.0)
    for i in range(int(360.0)):
        BOX[u'my box'] = turtle.get_heading() * 600.0
        turtle.set_shade(convert(BOX[u'my box'], TYPE_NUMBER) / 360.0)
        logo.icall(ACTION[u'action'])
        yield True
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(4.0)):
        turtle.arc(180.0, 75.0)
        turtle.arc(-180.0, 75.0)
        yield True
    for i in range(int(4.0)):
        turtle.arc(-180.0, -75.0)
        turtle.arc(180.0, -75.0)
        yield True
    turtle.right(1.0)
    yield True
ACTION["action"] = action


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
