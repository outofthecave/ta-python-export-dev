#!/usr/bin/env python

from math import sqrt
from random import uniform
from time import (sleep, time)

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def draw_b():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX['box1'] = convert(BOX[u'side b'], TYPE_NUMBER) / 2.0
    turtle.forward(convert(BOX['box1'], TYPE_NUMBER))
    logo.show(u'b', True)
    turtle.forward(convert(BOX['box1'], TYPE_NUMBER))
    yield True
ACTION["draw b"] = draw_b

def find_h():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'hypotenuse'] = sqrt(convert(BOX[u'side a'], TYPE_NUMBER) * convert(BOX[u'side a'], TYPE_NUMBER) + convert(BOX[u'side b'], TYPE_NUMBER) * convert(BOX[u'side b'], TYPE_NUMBER))
    BOX[u'radius'] = convert(BOX[u'hypotenuse'], TYPE_NUMBER) / 2.0
    yield True
ACTION["find h"] = find_h

def draw_a():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX['box1'] = convert(BOX[u'side a'], TYPE_NUMBER) / 2.0
    turtle.forward(convert(BOX['box1'], TYPE_NUMBER))
    logo.show(u'a', True)
    turtle.forward(convert(BOX['box1'], TYPE_NUMBER))
    yield True
ACTION["draw a"] = draw_a

def draw_h():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.arc(360.0, convert(BOX[u'radius'], TYPE_NUMBER))
    tw.print_(BOX[u'angle'], False)
    turtle.right(90.0)
    turtle.forward(convert(BOX[u'radius'], TYPE_NUMBER))
    logo.show(u'h', True)
    turtle.forward(convert(BOX[u'radius'], TYPE_NUMBER))
    yield True
ACTION["draw h"] = draw_h

def find_a():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'angle'] = 0.0
    turtle.set_shade(95.0)
    for i in range(int(360.0)):
        turtle.arc(180.0, convert(BOX[u'radius'], TYPE_NUMBER))
        if (float(turtle.get_y()) / tw.get_coord_scale() > 0.0):
            turtle.set_shade(50.0)
            return 
        turtle.set_pen_state(False)
        BOX[u'angle'] = convert(BOX[u'angle'], TYPE_NUMBER) + 1.0
        turtle.arc(180.0, convert(BOX[u'radius'], TYPE_NUMBER))
        turtle.right(1.0)
        turtle.set_pen_state(True)
        yield True
    yield True
ACTION["find a"] = find_a

def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    tw.clear_plugins()
    logo.stop_playing_media()
    logo.reset_scale()
    logo.reset_timer()
    logo.clear_value_blocks()
    logo.reset_internals()
    canvas.clearscreen()
    turtles.reset_turtles()
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['width'] / -4.0, 0.0)
    turtle.set_pen_state(True)
    BOX[u'side a'] = 200.0
    BOX[u'side b'] = 450.0
    logo.icall(ACTION[u'draw a'])
    yield True
    turtle.right(90.0)
    logo.icall(ACTION[u'draw b'])
    yield True
    logo.icall(ACTION[u'find h'])
    yield True
    logo.icall(ACTION[u'find a'])
    yield True
    logo.icall(ACTION[u'draw h'])
    yield True
    turtle.set_pen_state(False)
    turtle.set_xy(CONSTANTS['leftpos'], CONSTANTS['toppos'])
    turtle.set_pen_state(True)
    turtle.set_heading(0.0)
    logo.show(Media('media', u'./samples/images/Pythagoras.jpg'), False)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


