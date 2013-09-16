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

    logo.icall(ACTION[u'setup'])
    yield True
    logo.icall(ACTION[u'action'])
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(28.0)):
        turtle.arc(360.0, CONSTANTS['width'])
        logo.icall(ACTION[u'adjust pen'])
        yield True
    yield True
ACTION["action"] = action

def setup():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    canvas.fillscreen_with_gray(60.0, int(CONSTANTS['black']), 100.0)
    turtle.set_color(40.0)
    turtle.set_shade(20.0)
    turtle.set_pen_size(100.0)
    turtle.set_heading(15.0)
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], CONSTANTS['bottompos'])
    turtle.set_pen_state(True)
    yield True
ACTION["setup"] = setup

def adjust_pen():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_shade(turtle.get_shade() + 3.0)
    turtle.set_pen_size(turtle.get_pen_size() - 7.0)
    if (turtle.get_pen_size() < 1.0):
        turtle.set_pen_size(11.0)
    turtle.set_heading(turtle.get_heading() - -10.0)
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], CONSTANTS['bottompos'])
    turtle.set_pen_state(True)
    yield True
ACTION["adjust pen"] = adjust_pen


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
