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

    turtle.forward(float(CONSTANTS["white"]) - 160.0)
    turtle.right(90.0)
    turtle.forward(300.0 - 180.0)
    turtle.right(90.0)
    turtle.forward(10.0 - float(CONSTANTS["blue"]))
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


