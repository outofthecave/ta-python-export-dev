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
    turtle.set_color(60.0)
    for i in range(int(5000.0)):
        logo.icall(ACTION[u'random xy'])
        yield True
        BOX[u'my box'] = float(turtle.get_y()) / tw.get_coord_scale() + 900.0
        turtle.set_pen_size(convert(BOX[u'my box'], TYPE_NUMBER) / 9.0)
        turtle.set_shade(convert(BOX[u'my box'], TYPE_NUMBER) / 12.0)
        turtle.forward(1.0)
        yield True
    yield True
ACTION["start"] = start

def random_xy():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.set_xy(int(round(uniform(int(-600.0), int(600.0)), 0)), int(round(uniform(int(-450.0), int(450.0)), 0)))
    turtle.set_pen_state(True)
    yield True
ACTION["random xy"] = random_xy


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
