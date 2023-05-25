import pyautogui as bot

# click method
# parameters: x, y, button, clicks, interval

# default is left click
bot.click()

# click at specified position
bot.click(x=100, y=100, button="right")

# multiple clicks
bot.click(clicks=2, interval=1)

# doubleClick(), tripleClick()