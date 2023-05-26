import pyautogui as bot

# locateOnScreen method - locate image on screen
btn_7_location = bot.locateOnScreen('./btn-7.png')
print(btn_7_location) # returns a tuple (left, top, width, height)

# center the image
center_of_btn = bot.center(btn_7_location)
print(center_of_btn)

# locateCenterOnScreen combines locateOnScreen and center
direct_center = bot.locateCenterOnScreen('./btn-7.png')
print(direct_center == center_of_btn)

btn_7_x, btn_7_y = center_of_btn
print(btn_7_x, btn_7_y)

# shortcut to click the image
bot.click('btn-7.png')

# using confidence keyword
center_of_btn_conf = bot.locateOnScreen('btn-7.png', confidence=0.8)

# other methods
# - locateAllOnScreen
# - locate
# - locateAll

# 1) Grayscale Matching
# can pass grayscale as parameters to the method
gray_scale_match = bot.locateOnScreen('btn-7.png', grayscale=True)
# desaturates color from the images and screenshots to locate faster
# may cause false-positive


# 2) Pixel Matching
# pixel, getpixel methods to get the pixel RGB
im = bot.screenshot()
pixel1 = im.getpixel((100,200))
print(pixel1)

pixel2 = bot.pixel(100,200) # wrapper for getpixel
print(pixel2)

# to match
# check if the indicated pixel matches the color specified
# parameters: x, y, RGB tuple
match_val = bot.pixelMatchesColor(100, 200, (37,37,38))
print(match_val)

# optional tolerance argument to state how much each RGB can vary
match_val2 = bot.pixelMatchesColor(100,200, (35, 35, 35), tolerance = 10)
print(match_val2)
