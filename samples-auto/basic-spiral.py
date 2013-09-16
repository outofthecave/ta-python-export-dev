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
    BOX[u'my box'] = 0.0
    for i in range(int(300.0)):
        turtle.forward(convert(BOX[u'my box'], TYPE_NUMBER))
        turtle.right(91.0)
        BOX[u'my box'] = convert(BOX[u'my box'], TYPE_NUMBER) + 5.0
        turtle.set_color(turtle.get_heading() / 360.0 * 100.0)
        yield True
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
