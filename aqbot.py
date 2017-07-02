from selenium import webdriver
from tkinter import *
from threading import Timer
from repeatedTimer import RepeatedTimer
import gui

#declare some constants for clarity
#version number, TK app, and element in TK
CURRENT_VERSION = "0.3"
APP = 0
ELEMENT = 1

#boolean to change text and functionality of a button
buttonSwitch = True
#declare selenium chrome driver
browser = webdriver.Chrome(executable_path="chromedriver.exe")

#build the generated gui and hide the default tk gui
app = Tk()
app.withdraw()
appTuple = gui.create_aqBot(app)
appTuple[APP].title("aqBot v" + CURRENT_VERSION)
appTuple[ELEMENT].title.configure(text="aqBot v" + CURRENT_VERSION)

#The different methods for each given button in the gui
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

#set repeatable timer for the infinite stats function
infiniteStatsTimer = RepeatedTimer(1, infiniteStats)

#function that checks what the current text/functionality 
#of the button is for infinite stats
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

#function that automatically clicks the attack button
#after setting a monsters health to 0 (no user input needed)
def killMonster():
    setToZero()
    game = browser.find_element_by_tag_name("td")

    actions = webdriver.ActionChains(browser)
    actions.move_to_element_with_offset(game, 400, 200)
    actions.click()
    actions.perform()
        
#properly handle exiting the program by closing browser and destroying the gui
def exitHandler():
    browser.quit()
    app.destroy()

#add functionality to all gui buttons with their appropriate functions
appTuple[ELEMENT].openAQ.configure(command=openBrowser)
appTuple[ELEMENT].openAQG.configure(command=openBrowserGuardian)
appTuple[ELEMENT].kill.configure(command=killMonster)
appTuple[ELEMENT].infinite.configure(command=infiniteStatsControl)
appTuple[ELEMENT].refillMP.configure(command=refillMP)
appTuple[ELEMENT].refillSP.configure(command=refillSP)
appTuple[ELEMENT].refillHP.configure(command=fullHeal)
appTuple[ELEMENT].setZero.configure(command=setToZero)

appTuple[APP].protocol("WM_DELETE_WINDOW", exitHandler)
app.mainloop()
