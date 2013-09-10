#!/usr/bin/env python

from math import sqrt
from random import uniform
from time import (sleep, time)

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'trials'] = 1600.0
    logo.icall(ACTION[u'clear bins'])
    yield True
    logo.icall(ACTION[u'toss dice'])
    yield True
    logo.icall(ACTION[u'plot results'])
    yield True
ACTION["start"] = start

def toss_dice():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    for i in range(convert(BOX[u'trials'], TYPE_INT)):
        BOX[u'box'] = int(round(uniform(int(1.0), int(6.0)), 0)) + int(round(uniform(int(1.0), int(6.0)), 0))
        BOX[BOX[u'box']] = convert(BOX[BOX[u'box']], TYPE_NUMBER) + 1.0
        yield True
    yield True
ACTION["toss dice"] = toss_dice

def clear_bins():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'box'] = 2.0
    for i in range(int(11.0)):
        BOX[BOX[u'box']] = 0.0
        logo.icall(ACTION[u'next bin'])
        yield True
    yield True
ACTION["clear bins"] = clear_bins

def next_bin():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'box'] = convert(BOX[u'box'], TYPE_NUMBER) + 1.0
    yield True
ACTION["next bin"] = next_bin

def plot_results():
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
    turtle.set_shade(25.0)
    BOX[u'box'] = 2.0
    for i in range(int(11.0)):
        logo.icall(ACTION[u'bar graph'])
        yield True
    turtle.set_pen_state(False)
    turtle.set_xy(0.0, -50.0)
    turtle.set_pen_state(True)
    yield True
ACTION["plot results"] = plot_results

def bar_graph():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_pen_state(False)
    turtle.set_xy(50.0 * convert(BOX[u'box'], TYPE_NUMBER) - 6.0, 0.0)
    turtle.forward((-100.0))
    turtle.forward(100.0)
    turtle.set_pen_state(True)
    logo.icall(ACTION[u'bar'])
    yield True
ACTION["bar graph"] = bar_graph

def bar():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    turtle.set_color(convert(BOX[u'box'], TYPE_NUMBER) * 10.0)
    turtle.start_fill()
    for i in range(int(2.0)):
        turtle.forward(convert(BOX[BOX[u'box']], TYPE_NUMBER))
        turtle.right(90.0)
        turtle.forward(40.0)
        turtle.right(90.0)
        yield True
    turtle.stop_fill()
    logo.icall(ACTION[u'next bin'])
    yield True
ACTION["bar"] = bar




if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


