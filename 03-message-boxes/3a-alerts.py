import pyautogui as bot

bot.alert(text="This is an alert message box.", title="ALERT!!!", button='OK')

ans = bot.confirm(text="This is a confirmation message box.", title="Please confirm your options.", buttons=['OK', 'CANCEL'])
print(ans) # => OK

ans2 = bot.prompt(text="This is a prompt message box.", title="Please enter prompt", default="no input")
print(ans2)

ans3 = bot.password(text="This is a password message box.", title="Please enter your password", default="not entered", mask='*')
print('Your password is: ' + ans3)