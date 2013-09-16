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
    for i in range(int(500.0)):
        turtle.set_pen_state(False)
        turtle.set_xy(int(round(uniform(CONSTANTS['leftpos'], CONSTANTS['rightpos']), 0)), int(round(uniform(CONSTANTS['bottompos'], CONSTANTS['toppos']), 0)))
        turtle.set_pen_state(True)
        logo.icall(ACTION[u'xo man'])
        yield True
    yield True
ACTION["start"] = start

def xo_man():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_color(int(round(uniform(int(0.0), int(100.0)), 0)))
    turtle.set_pen_size(40.0)
    logo.icall(ACTION[u'xo'])
    yield True
    turtle.set_color(turtle.get_color() + 10.0)
    turtle.set_pen_size(turtle.get_pen_size() - 25.0)
    logo.icall(ACTION[u'xo'])
    yield True
ACTION["xo man"] = xo_man

def xo():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.right((-45.0))
    for i in range(int(4.0)):
        turtle.forward(75.0)
        turtle.forward((-75.0))
        turtle.right((-90.0))
        yield True
    turtle.right(45.0)
    turtle.set_pen_state(False)
    turtle.forward(90.0)
    turtle.set_pen_state(True)
    turtle.set_pen_size(turtle.get_pen_size() + 35.0)
    turtle.forward(1.0)
    turtle.set_pen_state(False)
    turtle.forward((-91.0))
    turtle.set_pen_state(True)
    turtle.set_pen_size(turtle.get_pen_size() - 35.0)
    yield True
ACTION["xo"] = xo


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
