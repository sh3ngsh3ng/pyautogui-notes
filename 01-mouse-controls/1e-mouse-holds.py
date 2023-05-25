import pyautogui as bot


# holding down the mouse button
bot.mouseDown()
bot.mouseUp()  # does the same thing as a left-button mouse click
bot.mouseDown(button='right')  # press the right button down
bot.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.