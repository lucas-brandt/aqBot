############################
# Generated code from PAGE #
############################

import sys
from tkinter import *
import tkinter.ttk as ttk

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import aqbot_gui
    aqbot_gui.vp_start_gui()
