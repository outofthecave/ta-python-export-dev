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

    turtle.right(90.0)
    turtle.forward(100.0)
    turtle.right((-90.0))
    turtle.forward(turtle.get_x() / tw.get_coord_scale())
    turtle.right((-90.0))
    turtle.forward(turtle.get_y() / tw.get_coord_scale())
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


