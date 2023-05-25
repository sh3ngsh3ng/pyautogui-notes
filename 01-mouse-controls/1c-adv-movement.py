import pyautogui as bot


bot.moveTo(100, 100, 2, bot.easeInQuad)     # start slow, end fast
bot.moveTo(1000, 100, 2, bot.easeOutQuad)    # start fast, end slow
bot.moveTo(100, 700, 2, bot.easeInOutQuad)  # start and end fast, slow in middle
bot.moveTo(1000, 700, 2, bot.easeInBounce)   # bounce at the end
bot.moveTo(100, 100, 2, bot.easeInElastic)  # rubber band at the end