#!/usr/bin/env python

from math import sqrt
from random import uniform
from time import sleep

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.forward(int(25.0 / 20.0) * 100.0)
    turtle.set_pen_state(False)
    turtle.set_xy(10.0, 0.0)
    turtle.set_pen_state(True)
    turtle.forward(25.0 / 20.0 * 100.0)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


