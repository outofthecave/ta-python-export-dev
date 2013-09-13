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

    tw.print_(100.0, False)
    sleep(1.0)
    yield True
    tw.print_(CONSTANTS['leftpos'], False)
    sleep(1.0)
    yield True
    tw.print_(u'text', False)
    sleep(1.0)
    yield True
    tw.print_(CONSTANTS['red'], False)
    yield True
ACTION["start"] = start




if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


