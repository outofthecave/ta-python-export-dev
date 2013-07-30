#!/usr/bin/env python

from window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    canvas = tw.canvas
    logo = tw.lc

    for i in range(logo.int(6.0)):
        turtle.forward(100.0)
        turtle.right(-120.0)
        turtle.forward(-100.0)
        turtle.right(60.0)
        yield True
    turtle.set_xy((0.0, 100.0))
    turtle.set_heading(210.0)
    for i in range(logo.int(2.0)):
        turtle.arc(180.0, 20.0)
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


