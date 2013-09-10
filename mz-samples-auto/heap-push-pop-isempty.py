#!/usr/bin/env python

from math import sqrt
from random import uniform
from time import (sleep, time)

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}
heap = []



def start():
    turtle = tw.turtles.get_active_turtle()
    turtles = tw.turtles
    canvas = tw.canvas
    logo = tw.lc

    BOX[u'i'] = 0.0
    for i in range(int(4.0)):
        heap.append(BOX[u'i'])
        BOX[u'i'] = convert(BOX[u'i'], TYPE_NUMBER) + 1.0
        yield True
    turtle.set_pen_state(False)
    while (not (not heap)):
        logo.show(heap.pop(), True)
        turtle.forward((-50.0))
        yield True
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


