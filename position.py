import pyautogui as bot

while True:
    mouse_position = bot.position()
    print(mouse_position)
    bot.sleep(3)