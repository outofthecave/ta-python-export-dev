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

    canvas.fillscreen(50.0, 30.0)
    for i in range(int(20.0)):
        turtle.set_pen_state(False)
        turtle.set_xy(int(round(uniform(CONSTANTS['leftpos'], CONSTANTS['rightpos']), 0)), int(round(uniform(CONSTANTS['bottompos'], CONSTANTS['toppos']), 0)))
        turtle.set_pen_state(True)
        turtle.set_heading(int(round(uniform(int(0.0), int(360.0)), 0)))
        logo.icall(ACTION[u'action'])
        yield True
    yield True
ACTION["start"] = start

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_size(20.0)
    turtle.set_color(20.0)
    turtle.set_shade(60.0)
    logo.icall(ACTION[u'draw'])
    yield True
    turtle.set_pen_size(12.0)
    turtle.set_color(0.0)
    turtle.set_shade(int(round(uniform(int(60.0), int(80.0)), 0)))
    logo.icall(ACTION[u'draw'])
    yield True
ACTION["action"] = action

def draw():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(int(3.0)):
        BOX[u'my box'] = 200.0
        for i in range(int(20.0)):
            turtle.arc(30.0, convert(BOX[u'my box'], TYPE_NUMBER))
            BOX[u'my box'] = convert(BOX[u'my box'], TYPE_NUMBER) / 1.2
            yield True
        yield True
    yield True
ACTION["draw"] = draw


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
