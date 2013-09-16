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
    canvas.fillscreen_with_gray(60.0, int(CONSTANTS['white']), 100.0)
    turtle.set_color(0.0)
    turtle.set_pen_size(20.0)
    BOX[u'my box'] = 0.0
    for i in range(int(1000.0)):
        logo.icall(ACTION[u'dot'])
        yield True
    yield True
ACTION["start"] = start

def dot():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(True)
    turtle.forward(1.0)
    turtle.set_pen_state(False)
    turtle.forward(convert(BOX[u'my box'], TYPE_NUMBER))
    turtle.right(93.0)
    BOX[u'my box'] = convert(BOX[u'my box'], TYPE_NUMBER) + 1.0
    turtle.set_color(convert(BOX[u'my box'], TYPE_NUMBER))
    yield True
ACTION["dot"] = dot


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
