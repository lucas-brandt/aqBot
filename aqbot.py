from selenium import webdriver
from tkinter import *

currentVersion = "0.1.1"
browser = webdriver.Chrome(executable_path="chromedriver.exe")

app = Tk()
app.title("aqBot v" + currentVersion)
app.minsize(width=300, height=200)
openButton = Button(app, text = "Open AdventureQuest")
openButton.pack()
openButtonGuardian = Button(app, text = "Open AdventureQuest (Guardians)")
openButtonGuardian.pack()

killButton = Button(app, text = "Kill Opponent")
killButton.pack()
mpButton = Button(app, text = "Refill MP for one turn")
mpButton.pack()
spButton = Button(app, text = "Refill SP for one turn")
spButton.pack()
healButton = Button(app, text = "Full Heal")
healButton.pack()


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

def exitHandler():
    browser.quit()
    app.destroy()

openButton.configure(command=openBrowser)
openButtonGuardian.configure(command=openBrowserGuardian)
killButton.configure(command=killOpponent)

app.protocol("WM_DELETE_WINDOW", exitHandler)
app.mainloop()
