#!/usr/bin/env python

from math import sqrt
from random import uniform

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(True)
    while turtle.get_pen_state():
        turtle.forward(100.0)
        turtle.right(90.0)
        turtle.set_pen_state(False)
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


