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
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], 0.0)
    turtle.set_pen_state(True)
    BOX[u'diameter'] = CONSTANTS['width'] / 10.0
    for i in range(int(10.0)):
        logo.icall(ACTION[u'circle'])
        yield True
    yield True
ACTION["start"] = start

def circle():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.arc(360.0, convert(BOX[u'diameter'], TYPE_NUMBER) / 2.0)
    turtle.set_pen_state(False)
    turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale() + convert(BOX[u'diameter'], TYPE_NUMBER), float(turtle.get_y()) / tw.get_coord_scale())
    turtle.set_pen_state(True)
    yield True
ACTION["circle"] = circle


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
