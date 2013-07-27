#!/usr/bin/env python

from window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    canvas = tw.canvas
    logo = tw.lc

    turtle.arc(90.0, 100.0)
ACTION["start"] = start




if __name__ == '__main__':
    start()
    gtk.main()


