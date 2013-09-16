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

    tw.clear_plugins()
    logo.stop_playing_media()
    logo.reset_scale()
    logo.reset_timer()
    logo.clear_value_blocks()
    logo.reset_internals()
    canvas.clearscreen()
    turtles.reset_turtles()
    turtle.set_pen_size(15.0)
    BOX[u'my box 1'] = 6200.0
    for i in range(int(6200.0)):
        BOX[u'my box 2'] = convert(BOX[u'my box 1'], TYPE_NUMBER) / 50.0
        turtle.set_shade(100.0 - convert(BOX[u'my box 2'], TYPE_NUMBER))
        turtle.forward(convert(BOX[u'my box 1'], TYPE_NUMBER) / 8.0)
        turtle.forward((-convert(BOX[u'my box 1'], TYPE_NUMBER) / 8.0))
        turtle.right(1.0)
        BOX[u'my box 1'] = convert(BOX[u'my box 1'], TYPE_NUMBER) - 1.0
        turtle.set_color(convert(BOX[u'my box 1'], TYPE_NUMBER))
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
