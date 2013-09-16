#!/usr/bin/env python

from time import *
from random import uniform
from math import *

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}


def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'angle'] = 0.5
    logo.icall(ACTION[u'unit circle'])
    yield True
    turtle.set_pen_state(False)
    turtle.set_color(CONSTANTS['blue'])
    turtle.set_xy(0.0, 0.0)
    turtle.set_heading(90.0)
    turtle.set_pen_state(True)
    turtle.forward((lambda x: cos(x))(convert(BOX[u'angle'], TYPE_FLOAT)) * 100.0)
    turtle.set_heading(0.0)
    turtle.set_color(CONSTANTS['green'])
    turtle.forward((lambda x: sin(x))(convert(BOX[u'angle'], TYPE_FLOAT)) * 100.0)
    turtle.set_color(CONSTANTS['black'])
    turtle.set_xy(0.0, 0.0)
    yield True
ACTION["start"] = start

def unit_circle():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.set_pen_size(3.0)
    turtle.set_xy(100.0, 0.0)
    turtle.set_heading(0.0)
    turtle.set_pen_state(True)
    turtle.arc(-360.0, 100.0)
    yield True
ACTION["unit circle"] = unit_circle


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
