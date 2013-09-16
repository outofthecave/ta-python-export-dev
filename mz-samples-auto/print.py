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

    tw.print_(100.0, False)
    print 100.0
    sleep(1.0)
    yield True
    tw.print_(CONSTANTS['leftpos'], False)
    print CONSTANTS['leftpos']
    sleep(1.0)
    yield True
    tw.print_(u'text', False)
    print u'text'
    sleep(1.0)
    yield True
    tw.print_(CONSTANTS['red'], False)
    print CONSTANTS['red']
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
