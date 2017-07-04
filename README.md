# aqBot
A simple program that automates the game play of the single player RPG game AdventureQuest. This program allows you to instantly kill opponents, change/manipulate in-game stats, and automatic training.

## FAQ
If you downloaded the program and have questions, most likely they will be answered in this section.

#### How do I download/use aqBot?
If you are interested in the code itself you can simply clone this repository and run/edit the file titled "aqbot.py". Alternatively, you can navigate to the the latest release (in the release tab) and download the zip file attached. From there all you will need to do is run the file named "aqbot.exe".

#### What is the difference between the "Open Adventure Quest" and the "Open Adventure Quest (G)" button?
The "Open Adventure Quest" button will open the default (f2p) version of AdventureQuest, while the "Open Adventure Quest (G)" button will open the (p2p) Guardian only version of AdventureQuest.

#### What are the two different sections for buttons and what do each do?
There are two different sections for automation within the GUI. The "Stat Modification" section allows the user to change all available local game variables such as health, opponent health, MP, and SP. The "Automation" section allows the user to automate their AdventureQuest gameplay without use of the user's mouse.

#### Why is an "autotrainer" not included?
Simply put, it is unnecessary. The fastest way to gain XP and Gold in the game is to compelete quests. Quests cannot be easily automated due to extensive dialog, and they require some user input. However, due to the automation scripts built into aqBot you can complete quests within seconds or minutes, instead of hours. This will allow you to hit your XP and gold cap much more quickly and efficiently than using an "autotrainer".

#### I set an opponent's health to 0 or used the "Kill Opponent" button and it didn't work. Why?
In order for those two buttons to function correctly you must wait until it is your characters turn (e.g. the NPC is no longer attacking).

#### How do the refill buttons work?
They each work by invisibly setting your stat to the highest possible amount (9999). The stat change is effective immediately, however you must wait until your next turn to see the stat change reflected. These buttons tend to only work for one/two turn(s), so it is recommended to use the "Infinite HP/SP/MP" button. This button will continuously update your skills to the highest amount.

#### When will the bot/script be updated and where can I find it?
You can find new updates on this github repo, or on the official release page. It will be updated as frequentely as time allows, or from user feedback. If you would like new features please let me know!
