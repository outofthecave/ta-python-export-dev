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

    tw.clear_plugins()
    canvas.clearscreen()
    turtles.reset_turtles()
    turtle.set_pen_state(False)
    turtle.forward((-turtle.get_shade()))
    turtle.set_pen_state(True)
    canvas.fillscreen_with_gray(15.0, 80.0, turtle.get_gray())
    turtle.set_color(60.0)
    turtle.set_shade(30.0)
    turtle.set_pen_size(6.0)
    turtle.start_fill()
    for i in range(logo.int(turtle.get_pen_size())):
        turtle.forward(100.0)
        turtle.right((-120.0))
        turtle.forward((-100.0))
        turtle.right(turtle.get_color())
        yield True
    turtle.stop_fill()
    turtle.set_xy((0.0, 50.0))
    turtle.set_heading(210.0)
    turtle.set_gray(0.0)
    for i in range(logo.int(2.0)):
        turtle.arc(180.0, 20.0)
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


