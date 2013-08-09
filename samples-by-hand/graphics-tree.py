#!/usr/bin/env python

import random

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}



def start():
    """action stack called 'start'
    """
    turtle = tw.turtles.get_active_turtle()
    canvas = tw.canvas
    logo = tw.lc
    
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
    turtle.set_pen_state(False)

    # setxy x=0 y=-400
    turtle.set_xy((0, -400), pendown=False)

    # pen down
    turtle.set_pen_state(True)

    # store in box="box 1" value=300
    BOX["box 1"] = 300

    # set color =10
    turtle.set_color(10)

    # action =action
    logo.icall(ACTION["action"])
    yield True
ACTION["start"] = start


def action():
    """action stack called 'action'
    """
    turtle = tw.turtles.get_active_turtle()
    logo = tw.lc
    
    # pen down
    turtle.set_pen_state(True)

    # if =(> =(box ="box 1") =10)
    if BOX["box 1"] > 10:
        # then
        # action ="action_2"
        logo.icall(ACTION["action_2"])
        yield True

    # TODO generate type conversion code when min and max are characters (see tabasics.Palettes._prim_random)
    # store in box="box 2" value=(random min=0 max=2)
    BOX["box 2"] = round(random.uniform(0, 2), 0)

    # if =(== =(box ="box 2") =0)
    if BOX["box 2"] == 0:
        # then
        # pen up
        turtle.set_pen_state(False)

        # forward =(/ =(box ="box 1") =2)
        turtle.forward(BOX["box 1"] / 2)

        # set color =40
        turtle.set_color(40)

        # set pen size =20
        turtle.set_pen_size(20)
        
        # forward =1
        turtle.forward(1)
        
        # pen down
        turtle.set_pen_state(True)
        
        # back =1
        turtle.forward(-1)
        
        # set color =10
        turtle.set_color(10)
        
        # set pen size =5
        turtle.set_pen_size(5)
        
        # pen up
        turtle.set_pen_state(False)
        
        # back =(/ =(box ="box 1") =2)
        turtle.forward(-BOX["box 1"] / 2)

    yield True
ACTION["action"] = action


def action_2():
    """action stack called 'action_2'
    """
    turtle = tw.turtles.get_active_turtle()
    logo = tw.lc
    
    # forward =(box ="box 1")
    turtle.forward(BOX["box 1"])
    
    # store in box="box 1" value=(/ =(box ="box 1") =1.5)
    BOX["box 1"] = BOX["box 1"] / 1.5
    
    # right =30
    turtle.right(30)
    
    # action ="action"
    logo.icall(ACTION["action"])
    yield True
    
    # left =60
    turtle.right(-60)
    
    # action ="action"
    logo.icall(ACTION["action"])
    yield True
    
    # right =30
    turtle.right(30)
    
    # store in box="box 1" value=(* =(box ="box 1") =1.5)
    BOX["box 1"] = BOX["box 1"] * 1.5
    
    # pen up
    turtle.set_pen_state(False)
    
    # back =(box ="box 1")
    turtle.forward(-BOX["box 1"])

    yield True
ACTION["action_2"] = action_2



if __name__ == '__main__':
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()


