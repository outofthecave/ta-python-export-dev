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

    BOX[u'my box_1'] = 0.0
    while True:
        if (convert(BOX[u'my box_1'], TYPE_NUMBER) > 3.0):
            return
        turtle.forward(100.0)
        turtle.right(90.0)
        BOX[u'my box_1'] = convert(BOX[u'my box_1'], TYPE_NUMBER) + 1.0
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
