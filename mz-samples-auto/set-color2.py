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

    turtle.set_color(60.0)
    turtle.forward(100.0)
    turtle.set_color(CONSTANTS['black'])
    turtle.forward(100.0)
    turtle.right(90.0)
    turtle.set_color(60.0)
    turtle.forward(100.0)
    turtle.set_color(CONSTANTS['orange'])
    turtle.forward(100.0)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


