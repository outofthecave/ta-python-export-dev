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

    turtle.forward(int(CONSTANTS["cyan"]) + 30.0)
    turtle.right(90.0)
    turtle.forward(40.0 + 40.0)
    turtle.right(90.0)
    turtle.forward(60.0 + int(CONSTANTS["yellow"]))
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


