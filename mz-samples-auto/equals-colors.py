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

    turtle.forward(100.0)
    if (int(CONSTANTS['red']) == 50.0):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (int(CONSTANTS['red']) == 0.0):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (CONSTANTS['red'] == CONSTANTS['black']):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (int(CONSTANTS['black']) == 0.0):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (CONSTANTS['red'].get_number_string() == u'red'):
        turtle.right(90.0)
    turtle.forward(100.0)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


