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
    if (1.2 < 1.0):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (u'text' > u'foo'):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (99.0 > float(u'100.0')):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (96.0 < ord(u'a')):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (CONSTANTS["red"] < CONSTANTS["blue"]):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (CONSTANTS["blue"] > 69.0):
        turtle.right(90.0)
    turtle.forward(100.0)
    if (CONSTANTS["blue"] > u'`foo'):
        turtle.right(90.0)
    turtle.forward(100.0)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


