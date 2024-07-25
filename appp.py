import pyautogui
from time import sleep

# 1- Clicar e copiar info do Email
pyautogui.click(1311, 791, clicks=3, duration=0.5)
pyautogui.hotkey('ctrl', 'c')

# 2- Colar no formulário
pyautogui.click(1183, 372, duration=0.5)
pyautogui.hotkey('ctrl', 'v')

# 3- Rolar Scrol
pyautogui.scroll(-70)
sleep(2)
