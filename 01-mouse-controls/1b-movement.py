import pyautogui as bot

# moving (absolute) to X and Y coordinates
bot.moveTo(100, 200)

# moving to coordinates in duration (3rd parameter)
bot.moveTo(600, 200, 3)

# moving (relative)
bot.move(0, 300, 3)

# drag and dragTo has the same parameters as move and moveTo
bot.drag(0, -300, 3, button="left")
bot.dragTo(600, 300, 3, button="left")

