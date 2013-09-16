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
    turtle.set_xy(CONSTANTS['leftpos'] / 2.0, 290.0)
    turtle.right(45.0)
    logo.icall(ACTION[u'horizontal'])
    yield True
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], CONSTANTS['bottompos'])
    turtle.set_pen_state(True)
    turtle.set_heading(0.0)
    logo.icall(ACTION[u'vertical'])
    yield True
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'] / 3.0, 80.0)
    turtle.right(135.0)
    turtle.set_pen_state(True)
    logo.icall(ACTION[u'vertical'])
    yield True
    logo.icall(ACTION[u'vertical'])
    yield True
ACTION["start"] = start

def horizontal():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(CONSTANTS['width'] / 6.0)):
        logo.icall(ACTION[u'action'])
        yield True
        turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale(), float(turtle.get_y()) / tw.get_coord_scale() - turtle.get_pen_size())
        yield True
    yield True
ACTION["horizontal"] = horizontal

def vertical():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(CONSTANTS['width'] / 15.0)):
        logo.icall(ACTION[u'action'])
        yield True
        turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale() + turtle.get_pen_size(), float(turtle.get_y()) / tw.get_coord_scale())
        yield True
    yield True
ACTION["vertical"] = vertical

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_size(7.0)
    turtle.set_color(70.0)
    turtle.set_shade(0.0)
    turtle.forward(1700.0)
    turtle.forward((-1700.0))
    turtle.set_shade(50.0)
    turtle.set_pen_size(int(round(uniform(int(3.0), int(10.0)), 0)))
    turtle.set_color(int(round(uniform(int(0.0), int(20.0)), 0)))
    turtle.forward(1700.0)
    turtle.forward((-1700.0))
    yield True
ACTION["action"] = action


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
