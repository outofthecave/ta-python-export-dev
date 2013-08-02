#!/usr/bin/env python

from window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.forward(100.0)
    tw.clear_plugins()
    logo.prim_clear_helper()
    canvas.clearscreen()
    turtles.reset_turtles()
    turtle.right(90.0)
    turtle.forward(100.0)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


