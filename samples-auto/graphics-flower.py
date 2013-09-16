#!/usr/bin/env python

from time import *
from random import uniform
from math import *

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}


def action2():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(4.0)):
        turtle.forward(convert(BOX[u'my box'], TYPE_NUMBER))
        turtle.right(90.0)
        yield True
    yield True
ACTION["action2"] = action2

def action1():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(10.0)):
        logo.icall(ACTION[u'action2'])
        yield True
        turtle.right(36.0)
        yield True
    yield True
ACTION["action1"] = action1

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
    BOX[u'my box'] = 0.0
    for i in range(int(300.0)):
        turtle.set_shade(100.0 - convert(BOX[u'my box'], TYPE_NUMBER))
        turtle.set_color(convert(BOX[u'my box'], TYPE_NUMBER) / 3.0)
        logo.icall(ACTION[u'action1'])
        yield True
        BOX[u'my box'] = convert(BOX[u'my box'], TYPE_NUMBER) + 1.0
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
