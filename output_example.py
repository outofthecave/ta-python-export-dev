#!/usr/bin/env python

from window_setup import *


canvas = get_canvas()

BOX = {}
ACTION = {}



def start():
    """auto-converted block code (the one that had a 'start' block at the top)
    """
    # example: draw a square
    for i in range(4):
        canvas.forward(100)
        canvas.right(90)

    # The idea is to handle everything as it is handled when the block code is 
    # executed in TA. That is, translate all blocks to operations on the canvas 
    # or Python control structures (e.g., loops).
ACTION["start"] = start


def foo():
    """other auto-converted stack of blocks (named 'foo')
    """
    # some code ...
    pass
ACTION["foo"] = foo


def unnamed_stack_1():
    """other auto-converted stack of blocks (unnamed)
    """
    # some code ...
    pass



if __name__ == '__main__':
    start()
    gtk.main()


