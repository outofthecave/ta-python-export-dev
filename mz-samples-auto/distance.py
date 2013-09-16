#!/usr/bin/env python

from time import *
from random import uniform
from math import *

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}


def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'scale'] = 50.0
    BOX[u'pi'] = 3.14
    turtle.set_pen_state(False)
    turtle.set_xy(0.0, 0.0)
    logo.icall(ACTION[u'point'])
    yield True
    turtle.set_xy(4.0 * convert(BOX[u'scale'], TYPE_NUMBER), 3.0 * convert(BOX[u'scale'], TYPE_NUMBER))
    logo.icall(ACTION[u'point'])
    yield True
    BOX[u'distance'] = sqrt((lambda x, y: x**2 + y**2)(4.0, 3.0))
    logo.show(BOX[u'distance'], True)
    yield True
ACTION["start"] = start

def point():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(True)
    turtle.forward(1.0)
    turtle.set_pen_state(False)
    yield True
ACTION["point"] = point

def draw_dist():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_heading(270.0)
    turtle.right((-(lambda x: 1 / sin(x))(float(3.0 / convert(BOX[u'distance'], TYPE_NUMBER))) * 180.0 / convert(BOX[u'pi'], TYPE_NUMBER)))
    turtle.set_pen_state(True)
    turtle.forward(convert(BOX[u'distance'], TYPE_NUMBER) * convert(BOX[u'scale'], TYPE_NUMBER))
    yield True
ACTION["draw_dist"] = draw_dist


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
