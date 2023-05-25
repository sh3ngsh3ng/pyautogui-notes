# Screen are referred by X and Y Cartesian coordiates
# starts from 0 on left side and 0 from top

# import the library
import pyautogui as bot

# get screen size
screen_size = bot.size()
print(screen_size)

# get position of mouse
mouse_position = bot.position()
print(mouse_position)


# check if XY coordinates are on the screen
print(bot.onScreen(1950, 10000))