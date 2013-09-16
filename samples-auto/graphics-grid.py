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

    BOX[u'grid spacing'] = 32.0
    logo.icall(ACTION[u'grid 1'])
    yield True
    logo.icall(ACTION[u'grid 2'])
    yield True
    logo.icall(ACTION[u'grid 3'])
    yield True
ACTION["start"] = start

def square():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.start_fill()
    for i in range(int(4.0)):
        turtle.forward(convert(BOX[u'side'], TYPE_NUMBER))
        turtle.right(90.0)
        yield True
    turtle.stop_fill()
    yield True
ACTION["square"] = square

def grid_2():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'side'] = 24.0
    BOX[u'offset'] = 4.0
    BOX[u'color scheme'] = u'color 2'
    logo.icall(ACTION[u'grid'])
    yield True
ACTION["grid 2"] = grid_2

def grid():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'] + convert(BOX[u'offset'], TYPE_NUMBER), CONSTANTS['bottompos'] + convert(BOX[u'offset'], TYPE_NUMBER))
    turtle.set_pen_state(True)
    for i in range(int(float(CONSTANTS['height']) / convert(BOX[u'grid spacing'], TYPE_NUMBER))):
        for i in range(int(float(CONSTANTS['width']) / convert(BOX[u'grid spacing'], TYPE_NUMBER))):
            turtle.set_heading(int(round(uniform(int(-15.0), int(15.0)), 0)))
            logo.icall(ACTION[convert(BOX[u'color scheme'], TYPE_STRING)])
            yield True
            logo.icall(ACTION[u'square'])
            yield True
            logo.icall(ACTION[u'inc x'])
            yield True
        logo.icall(ACTION[u'inc y'])
        yield True
    yield True
ACTION["grid"] = grid

def inc_x():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.set_xy(float(turtle.get_x()) / tw.get_coord_scale() + convert(BOX[u'grid spacing'], TYPE_NUMBER), float(turtle.get_y()) / tw.get_coord_scale())
    turtle.set_pen_state(True)
    yield True
ACTION["inc x"] = inc_x

def inc_y():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'] + convert(BOX[u'offset'], TYPE_NUMBER), float(turtle.get_y()) / tw.get_coord_scale() + convert(BOX[u'grid spacing'], TYPE_NUMBER))
    turtle.set_pen_state(True)
    yield True
ACTION["inc y"] = inc_y

def color_1():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_shade(50.0)
    turtle.set_color(int(round(uniform(int(5.0), int(15.0)), 0)))
    turtle.set_gray(int(round(uniform(int(80.0), int(100.0)), 0)))
    yield True
ACTION["color 1"] = color_1

def grid_1():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'side'] = 32.0
    BOX[u'offset'] = 0.0
    BOX[u'color scheme'] = u'color 1'
    logo.icall(ACTION[u'grid'])
    yield True
ACTION["grid 1"] = grid_1

def color_3():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_shade(50.0)
    turtle.set_color(int(round(uniform(int(10.0), int(20.0)), 0)))
    turtle.set_gray(int(round(uniform(int(80.0), int(100.0)), 0)))
    yield True
ACTION["color 3"] = color_3

def color_2():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_shade(40.0)
    turtle.set_color(int(round(uniform(int(35.0), int(65.0)), 0)))
    turtle.set_gray(int(round(uniform(int(80.0), int(100.0)), 0)))
    yield True
ACTION["color 2"] = color_2

def grid_3():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'side'] = 16.0
    BOX[u'offset'] = 8.0
    BOX[u'color scheme'] = u'color 3'
    logo.icall(ACTION[u'grid'])
    yield True
ACTION["grid 3"] = grid_3


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
