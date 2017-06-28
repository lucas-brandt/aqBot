from selenium import webdriver
from tkinter import *
from threading import Timer
from repeatedTimer import RepeatedTimer

CURRENT_VERSION = "0.2.1"

buttonSwitch = True
browser = webdriver.Chrome(executable_path="chromedriver.exe")

app = Tk()
app.title("aqBot v" + CURRENT_VERSION)
app.minsize(width=300, height=300)
openButton = Button(app, text = "Open AdventureQuest")
openButton.pack()
openButtonGuardian = Button(app, text = "Open AdventureQuest (Guardians)")
openButtonGuardian.pack()

zeroButton = Button(app, text="Set Opponent Health to 0")
zeroButton.pack()
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

def setToZero():
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

def killMonster():
    setToZero()
    game = browser.find_element_by_tag_name("td")

    actions = webdriver.ActionChains(browser)
    actions.move_to_element_with_offset(game, 400, 200)
    actions.click()
    actions.perform()
        
def exitHandler():
    browser.quit()
    app.destroy()

openButton.configure(command=openBrowser)
openButtonGuardian.configure(command=openBrowserGuardian)
zeroButton.configure(command=setToZero)
killButton.configure(command=killMonster)
mpButton.configure(command=refillMP)
spButton.configure(command=refillSP)
healButton.configure(command=fullHeal)
infiniteButton.configure(command=infiniteStatsControl)

app.protocol("WM_DELETE_WINDOW", exitHandler)
app.mainloop()
