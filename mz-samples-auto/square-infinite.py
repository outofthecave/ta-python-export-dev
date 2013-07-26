#!/usr/bin/env python

from window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    turtle = tw.turtles.get_active_turtle()
    canvas = tw.canvas
    logo = tw.lc

    while True:
        turtle.forward(100.0)
        turtle.right(90.0)
ACTION["start"] = start




if __name__ == '__main__':
    start()
    gtk.main()


