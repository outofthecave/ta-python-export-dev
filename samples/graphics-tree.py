#!/usr/bin/env python

import random

from classes import *


canvas = get_canvas()

BOX = {}
ACTION = {}



def start():
    """action stack called 'start'
    """
    # clear
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

    # pen up
    canvas.setpen(False)

    # setxy x=0 y=-400
    canvas.setxy(0, -400, pendown=False)

    # pen down
    canvas.setpen(True)

    # store in box="box 1" value=300
    BOX["box 1"] = 300

    # set color =10
    canvas.setcolor(10)

    # action =action
    ACTION["action"]()
ACTION["start"] = start


def action():
    """action stack called 'action'
    """
    # pen down
    canvas.setpen(True)

    # if =(> =(box ="box 1") =10)
    if BOX["box 1"] > 10:
        # then
        # action ="action_2"
        ACTION["action_2"]()

    # TODO generate type conversion code when min and max are characters (see tabasics.Palettes._prim_random)
    # store in box="box 2" value=(random min=0 max=2)
    BOX["box 2"] = round(random.uniform(0, 2), 0)

    # if =(== =(box ="box 2") =0)
    if BOX["box 2"] == 0:
        # then
        # pen up
        canvas.setpen(False)

        # forward =(/ =(box ="box 1") =2)
        canvas.forward(BOX["box 1"] / 2)

        # set color =40
        canvas.setcolor(40)

        # set pen size =20
        canvas.setpensize(20)
        
        # forward =1
        canvas.forward(1)
        
        # pen down
        canvas.setpen(True)
        
        # back =1
        canvas.forward(-1)
        
        # set color =10
        canvas.setcolor(10)
        
        # set pen size =5
        canvas.setpensize(5)
        
        # pen up
        canvas.setpen(False)
        
        # back =(/ =(box ="box 1") =2)
        canvas.forward(-BOX["box 1"] / 2)
ACTION["action"] = action


def action_2():
    """action stack called 'action_2'
    """
    # forward =(box ="box 1")
    canvas.forward(BOX["box 1"])
    
    # store in box="box 1" value=(/ =(box ="box 1") =1.5)
    BOX["box 1"] = BOX["box 1"] / 1.5
    
    # right =30
    canvas.right(30)
    
    # action ="action"
    ACTION["action"]()
    
    # left =60
    canvas.right(-60)
    
    # action ="action"
    ACTION["action"]()
    
    # right =30
    canvas.right(30)
    
    # store in box="box 1" value=(* =(box ="box 1") =1.5)
    BOX["box 1"] = BOX["box 1"] * 1.5
    
    # pen up
    canvas.setpen(False)
    
    # back =(box ="box 1")
    canvas.forward(-BOX["box 1"])
ACTION["action_2"] = action_2



if __name__ == '__main__':
    start()
    gtk.main()


