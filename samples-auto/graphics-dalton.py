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
    canvas.fillscreen_with_gray(60.0, int(CONSTANTS['black']), 100.0)
    turtle.set_pen_size(25.0)
    BOX[u'my box_1'] = 1.0
    for i in range(int(100.0)):
        logo.icall(ACTION[u'action'])
        yield True
        turtle.right(119.8)
        BOX[u'my box_1'] = convert(BOX[u'my box_1'], TYPE_NUMBER) + 1.0
        yield True
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(convert(BOX[u'my box_1'], TYPE_INT)):
        turtle.set_color(int(round(uniform(int(60.0), int(80.0)), 0)))
        turtle.set_shade(int(round(uniform(int(40.0), int(100.0)), 0)))
        turtle.set_pen_state(True)
        turtle.forward(1.0)
        turtle.set_pen_state(False)
        turtle.forward(25.0)
        yield True
    yield True
ACTION["action"] = action


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
