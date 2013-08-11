#!/usr/bin/env python

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
    turtle.set_color(turtle.get_shade())
    turtle.right(90.0)
    turtle.forward(100.0)
    turtle.set_gray(turtle.get_color())
    turtle.right(90.0)
    turtle.forward(turtle.get_gray())
    turtle.set_color(CONSTANTS["white"])
    turtle.forward(50.0)
    turtle.set_color(CONSTANTS["yellow"])
    turtle.right(90.0)
    turtle.forward(100.0)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


