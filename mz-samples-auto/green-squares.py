#!/usr/bin/env python

from time import *
from random import uniform
from math import *

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}


def start():
    tw.start_plugins()
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.right((-90.0))
    turtle.set_color(40.0)
    turtle.set_shade(20.0)
    turtle.set_gray(70.0)
    logo.icall(ACTION[u'square'])
    yield True
    turtle.set_color(CONSTANTS['green'])
    logo.icall(ACTION[u'square'])
    yield True
    turtle.set_color(40.0)
    turtle.set_shade(int(CONSTANTS['yellow']))
    logo.icall(ACTION[u'square'])
    yield True
    turtle.set_shade(20.0)
    turtle.set_gray(int(CONSTANTS['blue']))
    logo.icall(ACTION[u'square'])
    yield True
ACTION["start"] = start

def square():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.start_fill()
    for i in range(int(4.0)):
        turtle.forward(50.0)
        turtle.right(90.0)
        yield True
    turtle.stop_fill()
    turtle.forward((-10.0))
    turtle.right(90.0)
    yield True
ACTION["square"] = square


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
