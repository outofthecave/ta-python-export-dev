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

    turtle.forward(int(CONSTANTS['white']) % 60.0)
    turtle.right(90.0)
    turtle.forward(1000.0 % 300.0)
    turtle.right(90.0)
    turtle.forward(110.0 % int(CONSTANTS['blue']))
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


