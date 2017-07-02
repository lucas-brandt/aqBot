############################
# Generated code from PAGE #
############################

from tkinter import *
import tkinter.ttk as ttk

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = aqBot (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_aqBot(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = aqBot (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_aqBot():
    global w
    w.destroy()
    w = None


class aqBot:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("800x600+1038+241")
        top.title("aqBot")
        top.configure(background="#d9d9d9")



        self.title = Message(top)
        self.title.place(relx=0.26, rely=-0.17, relheight=0.45, relwidth=0.47)
        self.title.configure(background="#d9d9d9")
        self.title.configure(font=font9)
        self.title.configure(foreground="#000000")
        self.title.configure(highlightbackground="#d9d9d9")
        self.title.configure(highlightcolor="black")
        self.title.configure(text='''aqBot v1.0''')
        self.title.configure(width=378)

        self.openAQ = Button(top)
        self.openAQ.place(relx=0.08, rely=0.18, height=54, width=300)
        self.openAQ.configure(activebackground="#d9d9d9")
        self.openAQ.configure(activeforeground="#000000")
        self.openAQ.configure(background="#d9d9d9")
        self.openAQ.configure(disabledforeground="#a3a3a3")
        self.openAQ.configure(foreground="#000000")
        self.openAQ.configure(highlightbackground="#d9d9d9")
        self.openAQ.configure(highlightcolor="black")
        self.openAQ.configure(pady="0")
        self.openAQ.configure(text='''Open Adventure Quest''')

        self.openAQG = Button(top)
        self.openAQG.place(relx=0.57, rely=0.18, height=54, width=300)
        self.openAQG.configure(activebackground="#d9d9d9")
        self.openAQG.configure(activeforeground="#000000")
        self.openAQG.configure(background="#d9d9d9")
        self.openAQG.configure(disabledforeground="#a3a3a3")
        self.openAQG.configure(foreground="#000000")
        self.openAQG.configure(highlightbackground="#d9d9d9")
        self.openAQG.configure(highlightcolor="black")
        self.openAQG.configure(pady="0")
        self.openAQG.configure(text='''Open Adventure Quest (G)''')

        self.stats = Message(top)
        self.stats.place(relx=0.13, rely=0.33, relheight=0.18, relwidth=0.28)
        self.stats.configure(background="#d9d9d9")
        self.stats.configure(font=font10)
        self.stats.configure(foreground="#000000")
        self.stats.configure(highlightbackground="#d9d9d9")
        self.stats.configure(highlightcolor="black")
        self.stats.configure(text='''Stat Modification''')
        self.stats.configure(width=225)

        self.auto = Message(top)
        self.auto.place(relx=0.63, rely=0.33, relheight=0.18, relwidth=0.28)
        self.auto.configure(background="#d9d9d9")
        self.auto.configure(font=font10)
        self.auto.configure(foreground="#000000")
        self.auto.configure(highlightbackground="#d9d9d9")
        self.auto.configure(highlightcolor="black")
        self.auto.configure(text='''Automation''')
        self.auto.configure(width=225)

        self.kill = Button(top)
        self.kill.place(relx=0.64, rely=0.5, height=54, width=210)
        self.kill.configure(activebackground="#d9d9d9")
        self.kill.configure(activeforeground="#000000")
        self.kill.configure(background="#d9d9d9")
        self.kill.configure(disabledforeground="#a3a3a3")
        self.kill.configure(foreground="#000000")
        self.kill.configure(highlightbackground="#d9d9d9")
        self.kill.configure(highlightcolor="black")
        self.kill.configure(pady="0")
        self.kill.configure(text='''Kill Opponent''')

        self.infinite = Button(top)
        self.infinite.place(relx=0.64, rely=0.63, height=54, width=210)
        self.infinite.configure(activebackground="#d9d9d9")
        self.infinite.configure(activeforeground="#000000")
        self.infinite.configure(background="#d9d9d9")
        self.infinite.configure(disabledforeground="#a3a3a3")
        self.infinite.configure(foreground="#000000")
        self.infinite.configure(highlightbackground="#d9d9d9")
        self.infinite.configure(highlightcolor="black")
        self.infinite.configure(pady="0")
        self.infinite.configure(text='''Infinite HP/SP/MP''')

        self.refillMP = Button(top)
        self.refillMP.place(relx=0.16, rely=0.5, height=54, width=170)
        self.refillMP.configure(activebackground="#d9d9d9")
        self.refillMP.configure(activeforeground="#000000")
        self.refillMP.configure(background="#d9d9d9")
        self.refillMP.configure(disabledforeground="#a3a3a3")
        self.refillMP.configure(foreground="#000000")
        self.refillMP.configure(highlightbackground="#d9d9d9")
        self.refillMP.configure(highlightcolor="black")
        self.refillMP.configure(pady="0")
        self.refillMP.configure(text='''Refill MP''')

        self.refillSP = Button(top)
        self.refillSP.place(relx=0.16, rely=0.63, height=54, width=170)
        self.refillSP.configure(activebackground="#d9d9d9")
        self.refillSP.configure(activeforeground="#000000")
        self.refillSP.configure(background="#d9d9d9")
        self.refillSP.configure(disabledforeground="#a3a3a3")
        self.refillSP.configure(foreground="#000000")
        self.refillSP.configure(highlightbackground="#d9d9d9")
        self.refillSP.configure(highlightcolor="black")
        self.refillSP.configure(pady="0")
        self.refillSP.configure(text='''Refill SP''')

        self.refillHP = Button(top)
        self.refillHP.place(relx=0.16, rely=0.77, height=54, width=170)
        self.refillHP.configure(activebackground="#d9d9d9")
        self.refillHP.configure(activeforeground="#000000")
        self.refillHP.configure(background="#d9d9d9")
        self.refillHP.configure(disabledforeground="#a3a3a3")
        self.refillHP.configure(foreground="#000000")
        self.refillHP.configure(highlightbackground="#d9d9d9")
        self.refillHP.configure(highlightcolor="black")
        self.refillHP.configure(pady="0")
        self.refillHP.configure(text='''Refill HP''')

        self.setZero = Button(top)
        self.setZero.place(relx=0.16, rely=0.9, height=54, width=170)
        self.setZero.configure(activebackground="#d9d9d9")
        self.setZero.configure(activeforeground="#000000")
        self.setZero.configure(background="#d9d9d9")
        self.setZero.configure(disabledforeground="#a3a3a3")
        self.setZero.configure(foreground="#000000")
        self.setZero.configure(highlightbackground="#d9d9d9")
        self.setZero.configure(highlightcolor="black")
        self.setZero.configure(pady="0")
        self.setZero.configure(text='''Set Heath to 0''')






if __name__ == '__main__':
    vp_start_gui()

