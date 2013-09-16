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

    turtle.set_pen_size(5.0)
    canvas.fillscreen_with_gray(60.0, int(CONSTANTS['black']), 100.0)
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], CONSTANTS['toppos'])
    logo.icall(ACTION[u'action'])
    yield True
ACTION["start"] = start

def curl():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_color(int(round(uniform(int(0.0), int(100.0)), 0)))
    turtle.set_pen_state(True)
    BOX[u'radius'] = 10.0
    for i in range(int(36.0)):
        turtle.arc(90.0, convert(BOX[u'radius'], TYPE_NUMBER))
        BOX[u'radius'] = convert(BOX[u'radius'], TYPE_NUMBER) + turtle.get_pen_size() / 2.0
        yield True
    turtle.set_pen_state(False)
    yield True
ACTION["curl"] = curl

def action():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    while True:
        logo.icall(ACTION[u'curl'])
        yield True
        logo.icall(ACTION[u'next position'])
        yield True
        if (float(turtle.get_y()) / tw.get_coord_scale() < CONSTANTS['bottompos']):
            return
        yield True
    turtle.set_pen_state(True)
    yield True
ACTION["action"] = action

def next_position():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale() + turtle.get_pen_size() * 60.0, float(turtle.get_y()) / tw.get_coord_scale())
    if (float(turtle.get_x()) / tw.get_coord_scale() > CONSTANTS['rightpos']):
        turtle.set_xy(CONSTANTS['leftpos'], float(turtle.get_y()) / tw.get_coord_scale() - turtle.get_pen_size() * 40.0)
    yield True
ACTION["next position"] = next_position


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
