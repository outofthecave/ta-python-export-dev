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

    turtle.set_heading(16.0)
    while True:
        for i in range(logo.int(4.0)):
            turtle.set_gray(turtle.get_color())
            turtle.set_color(turtle.get_heading())
            turtle.right((-turtle.get_shade()))
            if (turtle.get_pen_state() and turtle.get_pen_state()):
                while (not (not turtle.get_pen_state())):
                    turtle.right(90.0)
                    turtle.forward(100.0)
                    turtle.set_pen_state(False)
                    yield True
            else:
                turtle.set_pen_state(True)
                turtle.right((-90.0))
                turtle.forward(100.0)
            yield True
        turtle.set_xy((turtle.get_y() / tw.get_coord_scale(), turtle.get_x() / tw.get_coord_scale()))
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


