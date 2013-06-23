#!/usr/bin/env python

import random

from classes import *


canvas = get_canvas()

BOX = {}
ACTION = {}



def start():
    """action stack called 'start'
    """
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
        canvas.setpen(False)
        
        # setxy =(random min=left max=right) =(random min=bottom max=top)
        canvas.setxy(random.uniform(CONSTANTS['leftpos'], 
                                    CONSTANTS['rightpos']), 
                     random.uniform(CONSTANTS['bottompos'], 
                                    CONSTANTS['toppos']))
        
        # pen down
        canvas.setpen(True)
        
        # action ="xo man"
        ACTION["xo man"]()
ACTION["start"] = start


def xo_man():
    """action stack called 'xo man'
    """
    # set color =(random min=0 max=100)
    canvas.setcolor(random.uniform(0, 100))
    
    # set pen size =40
    canvas.setpensize(40)
    
    # action ="xo"
    ACTION["xo"]()
    
    # set color =(+ =color =10)
    canvas.setcolor(canvas.color + 10)
    
    # set pen size =(- =(pen size) =25)
    canvas.setpensize(canvas.pensize - 25)
    
    # action ="xo"
    ACTION["xo"]()
ACTION["xo man"] = xo_man


def xo():
    """action stack called 'xo'
    """
    # left =45
    canvas.right(-45)
    
    # repeat =4
    for i in range(4):

        # forward =75
        canvas.forward(75)
        
        # back =75
        canvas.forward(-75)
        
        # left =90
        canvas.right(-90)
        
    # right =45
    canvas.right(45)
    
    # pen up
    canvas.setpen(False)
    
    # forward =90
    canvas.forward(90)
    
    # pen down
    canvas.setpen(True)
    
    # set pen size =(+ =(pen size) =35)
    canvas.setpensize(canvas.pensize + 35)
    
    # forward =1
    canvas.forward(1)
    
    # pen up
    canvas.setpen(False)
    
    # back =91
    canvas.forward(-91)
    
    # pen down
    canvas.setpen(True)
    
    # set pen size =(- =(pen size) =35)
    canvas.setpensize(canvas.pensize - 35)
ACTION["xo"] = xo



if __name__ == '__main__':
    start()
    gtk.main()


