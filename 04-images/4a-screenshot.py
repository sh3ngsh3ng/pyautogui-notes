import pyautogui as bot

# screenshot method

# returns an Image object (Pillow or PIL module documentation)
im1 = bot.screenshot()
print(im1)

# saves a file and also returns an Image object
im2 = bot.screenshot('testing_shot.png')

# screenshot a portion of the screen
# tuple with 4 elements - left, top, width, height
im3 = bot.screenshot('regioned.png', region=(0, 0, 500,500))

