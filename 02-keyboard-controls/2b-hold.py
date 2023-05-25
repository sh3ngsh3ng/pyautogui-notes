import pyautogui as bot

# hold function can be used as context manager
with bot.hold('shift'):
    bot.click()
    bot.press(['down','down','down','down'])


