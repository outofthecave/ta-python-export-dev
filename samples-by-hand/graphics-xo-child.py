#!/usr/bin/env python

import random

from window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    """action stack called 'start'
    """
    turtle = tw.turtles.get_active_turtle()
    canvas = tw.canvas
    logo = tw.lc

    # clean
    # copied from talogo.LogoCode.prim_clear
    # TODO find a way to clear the plugins without accessing gui.tw
    #gui.tw.clear_plugins()
    #if gui.tw.gst_available:
    #    from TurtleArt.tagplay import stop_media
    #    stop_media(gui.tw.lc)
    canvas.clearscreen()
    # TODO necessary?
    #gui.tw.lc.scale = DEFAULT_SCALE
    #gui.tw.lc.hidden_turtle = None

    # repeat =500
    for i in range(500):
        
        # pen up
        turtle.set_pen_state(False)
        
        # setxy =(random min=left max=right) =(random min=bottom max=top)
        turtle.set_xy((random.uniform(CONSTANTS['leftpos'], 
                                      CONSTANTS['rightpos']), 
                       random.uniform(CONSTANTS['bottompos'], 
                                      CONSTANTS['toppos'])), 
                      pendown=False)
        
        # pen down
        turtle.set_pen_state(True)
        
        # action ="xo man"
        logo.icall(ACTION["xo man"])

        yield True

    yield True
ACTION["start"] = start


def xo_man():
    """action stack called 'xo man'
    """
    turtle = tw.turtles.get_active_turtle()
    logo = tw.lc

    # set color =(random min=0 max=100)
    turtle.set_color(random.uniform(0, 100))
    
    # set pen size =40
    turtle.set_pen_size(40)
    
    # action ="xo"
    logo.icall(ACTION["xo"])

    yield True
    
    # set color =(+ =color =10)
    turtle.set_color(turtle.get_color() + 10)
    
    # set pen size =(- =(pen size) =25)
    turtle.set_pen_size(turtle.get_pen_size() - 25)
    
    # action ="xo"
    logo.icall(ACTION["xo"])

    yield True
ACTION["xo man"] = xo_man


def xo():
    """action stack called 'xo'
    """
    turtle = tw.turtles.get_active_turtle()
    logo = tw.lc

    # left =45
    turtle.right(-45)
    
    # repeat =4
    for i in range(4):

        # forward =75
        turtle.forward(75)
        
        # back =75
        turtle.forward(-75)
        
        # left =90
        turtle.right(-90)
        
    # right =45
    turtle.right(45)
    
    # pen up
    turtle.set_pen_state(False)
    
    # forward =90
    turtle.forward(90)
    
    # pen down
    turtle.set_pen_state(True)
    
    # set pen size =(+ =(pen size) =35)
    turtle.set_pen_size(turtle.get_pen_size() + 35)
    
    # forward =1
    turtle.forward(1)
    
    # pen up
    turtle.set_pen_state(False)
    
    # back =91
    turtle.forward(-91)
    
    # pen down
    turtle.set_pen_state(True)
    
    # set pen size =(- =(pen size) =35)
    turtle.set_pen_size(turtle.get_pen_size() - 35)

    yield True
ACTION["xo"] = xo



if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


