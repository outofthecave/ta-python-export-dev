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

    for i in range(int(4.0)):
        turtle.forward(100.0)
        turtle.right(50.0 + 40.0)
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()

