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

    logo.icall(ACTION[u'setup'])
    yield True
    for i in range(int(25.0)):
        for i in range(int(30.0)):
            turtle.forward(CONSTANTS['width'])
            turtle.forward((-CONSTANTS['width']))
            turtle.right(12.0)
            yield True
        logo.icall(ACTION[u'update pen'])
        yield True
    yield True
ACTION["start"] = start

def update_pen():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_size(turtle.get_pen_size() - 1.0)
    turtle.set_shade(turtle.get_shade() + 4.0)
    yield True
ACTION["update pen"] = update_pen

def setup():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    canvas.fillscreen_with_gray(60.0, 80.0, 100.0)
    turtle.set_pen_state(False)
    turtle.set_xy(-200.0, -100.0)
    turtle.set_pen_state(True)
    turtle.set_pen_size(30.0)
    turtle.set_color(15.0)
    turtle.set_shade(0.0)
    yield True
ACTION["setup"] = setup




if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


