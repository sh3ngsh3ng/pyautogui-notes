import pyautogui as bot

class Browser():
    def __init__(self, bot, browser_type=None):
        self.bot = bot
        self.browser_type = browser_type if browser_type is not None else 'chrome'

    def open_browser(self):
        self.bot.press('win')
        self.bot.sleep(1)
        self.bot.write(self.browser_type)
        self.bot.press('enter')
        # self.bot.sleep(1)
        # self.bot.hotkey('win', 'up')
        # self.bot.click()
    
    def go_to_url(self, url):
        self.bot.hotkey('alt', 'd')
        self.bot.write(url)
        self.bot.press('enter')

    def wait_for_page(self, page_image, count=3, interval=2):
        page_check = self.bot.locateOnScreen(page_image)

        # if page loaded, return True
        if page_check:
            return True

        # page not loaded, retry 3 times
        retry_count = 0
        while not page_check:
            if retry_count == count:
                break
            self.bot.sleep(interval)
            retry_count += 1
            page_check = self.bot.locateOnScreen(page_image)
        print(retry_count)
        if retry_count == count:
            return False
        else:
            return True

    def scroll_to_view(self, item_image, magnitude=1, direction='down'):
        item_check = self.bot.locateOnScreen(item_image)
        scroll_value = 100 * magnitude * (-1 if direction == 'down' else 1)
        while not item_check:
            self.bot.scroll(scroll_value)
            item_check = self.bot.locateOnScreen(item_image)
        self.bot.moveTo(self.bot.locateOnScreen(item_image))




browser = Browser(bot)
browser.open_browser()
browser.go_to_url('mothership.sg')
browser.wait_for_page('page_image.png')
# browser.wait_for_page('error_screen.png')
browser.scroll_to_view('item_image.png')
