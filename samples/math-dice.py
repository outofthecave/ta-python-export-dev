#!/usr/bin/env python

import random

# TODO avoid this
from TurtleArt.taconstants import DEFAULT_SCALE

from classes import *


canvas = get_canvas()

BOX = {}
ACTION = {}



def start():
    """action stack called 'start'
    """
    # store in box="trials" value=1600
    BOX["trials"] = 1600
    
    # action ="clear bins"
    ACTION["clear bins"]()
    
    # action ="toss dice"
    ACTION["toss dice"]()
    
    # action ="plot results"
    ACTION["plot results"]()
ACTION["start"] = start


def clear_bins():
    """action stack called 'clear bins'
    """
    # store in box="box" value=2
    BOX["box"] = 2
    
    # repeat =11
    for i in range(11):

        # store in box=(box ="box") value=0
        BOX[BOX["box"]] = 0
        
        # store in box="box" value=(+ =(box ="box") =1)
        BOX["box"] = BOX["box"] + 1
ACTION["clear bins"] = clear_bins


def toss_dice():
    """action stack called 'toss dice'
    """
    # repeat =(box ="trials")
    for i in range(BOX["trials"]):
        
        # store in box="box" value=(+ =(random min=1 max=6) =(random min=1 max=6))
        BOX["box"] = round(random.uniform(1, 6), 0) + round(random.uniform(1, 6), 0)
        
        # store in box=(box ="box") value=(+ =(box =(box ="box")) = 1)
        BOX[BOX["box"]] = BOX[BOX["box"]] + 1
ACTION["toss dice"] = toss_dice


def plot_results():
    """action stack called 'plot results'
    """
    # clean
    canvas.clearscreen()
    
    # set shade =25
    canvas.setshade(25)
    
    # store in box="box" value=2
    BOX["box"] = 2
    
    # repeat =11
    for i in range(11):
        
        # pen up
        canvas.setpen(False)
        
        # setxy x=(* =50 =(- =(box ="box") =6)) y=0
        canvas.setxy(50 * (BOX["box"] - 6), 0)
        
        # back =50
        canvas.forward(-50)
        
        # show =(box ="box")
        # TODO implement properly
        x = int(canvas.width / 2) + int(canvas.xcor)
        y = int(canvas.height / 2) - int(canvas.ycor)
        y -= canvas.textsize
        canvas.draw_text(str(BOX["box"]), x, y,
                         int(canvas.textsize *
                             DEFAULT_SCALE / 100.),
                         canvas.width - x)
        
        # forward =50
        canvas.forward(50)
        
        # pen down
        canvas.setpen(True)
        
        # set color =(* =(box ="box") =10)
        canvas.setcolor(BOX["box"] * 10)
        
        # start fill
        canvas.start_fill()
        
        # repeat =2
        for j in range(2):
            
            # forward =(box =(box ="box"))
            canvas.forward(BOX[BOX["box"]])
            
            # right =90
            canvas.right(90)
            
            # forward =40
            canvas.forward(40)
            
            # right =90
            canvas.right(90)
        
        # end fill
        canvas.stop_fill()
        
        # store in box="box" value=(+ =(box ="box") =1)
        BOX["box"] = BOX["box"] + 1
    
    # pen up
    canvas.setpen(False)
    
    # setxy x=0 y=-50
    canvas.setxy(0, -50)
    
    # pen down
    canvas.setpen(True)
ACTION["plot results"] = plot_results



if __name__ == '__main__':
    start()
    gtk.main()


