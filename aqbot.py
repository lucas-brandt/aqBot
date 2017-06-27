from selenium import webdriver
from tkinter import *
from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        
    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

CURRENT_VERSION = "0.2"

buttonSwitch = True
browser = webdriver.Chrome(executable_path="chromedriver.exe")

app = Tk()
app.title("aqBot v" + CURRENT_VERSION)
app.minsize(width=300, height=200)
openButton = Button(app, text = "Open AdventureQuest")
openButton.pack()
openButtonGuardian = Button(app, text = "Open AdventureQuest (Guardians)")
openButtonGuardian.pack()

killButton = Button(app, text="Kill Opponent")
killButton.pack()
mpButton = Button(app, text="Refill MP for one turn")
mpButton.pack()
spButton = Button(app, text="Refill SP for one turn")
spButton.pack()
healButton = Button(app, text="Full Heal")
healButton.pack()
infiniteButton = Button(app, text="Infinite HP/SP/MP")
infiniteButton.pack()


def openBrowser():
    browser.get('https://aq.battleon.com/Build30/game.asp?launchtype=medium/')

def openBrowserGuardian():
    browser.get('https://guardian.battleon.com/Build30/game.asp?launchtype=medium/')

def killOpponent():
    browser.execute_script("document.embeds[0].SetVariable(\"_root.monster.intHP\", 0)")

def refillMP():
    browser.execute_script("document.embeds[0].SetVariable(\"_root.player.intMP\", 9999)")

def refillSP():
    browser.execute_script("document.embeds[0].SetVariable(\"_root.player.intSP\", 9999)")

def fullHeal():
    browser.execute_script("document.embeds[0].SetVariable(\"_root.player.intHP\", 9999)")

def infiniteStats():
    refillMP()
    refillSP()
    fullHeal()

infiniteStatsTimer = RepeatedTimer(1, infiniteStats)

def infiniteStatsControl():
    global infiniteStatsTimer
    global infiniteButton
    global buttonSwitch

    if buttonSwitch:
        buttonSwitch = False
        infiniteButton.configure(text="Stop")
        infiniteStatsTimer.start()
    else:
        buttonSwitch = True
        infiniteButton.configure(text="Infinite HP/SP/MP")
        infiniteStatsTimer.stop()
        
def exitHandler():
    browser.quit()
    app.destroy()

openButton.configure(command=openBrowser)
openButtonGuardian.configure(command=openBrowserGuardian)
killButton.configure(command=killOpponent)
mpButton.configure(command=refillMP)
spButton.configure(command=refillSP)
healButton.configure(command=fullHeal)
infiniteButton.configure(command=infiniteStatsControl)

app.protocol("WM_DELETE_WINDOW", exitHandler)
app.mainloop()
