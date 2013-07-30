#!/usr/bin/env python

from window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    canvas = tw.canvas
    logo = tw.lc

    while True:
        turtle.forward(100.0)
        turtle.right(90.0)
        yield True

    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


