import pyautogui
import pyperclip
from time import sleep

# 1-Clicar e digitar meu usuário
pyautogui.click(975, 540, duration=0.5)
pyautogui.write('Wallisson')
# 2-Clicar e digitar minha senha
pyautogui.click(975, 573, duration=0.5)
pyautogui.write('12345678')
# 3-Clicar em "Entrar"
pyautogui.click(847, 616, duration=0.5)
# 4-Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
#   1-Clicar e digitar produto
        pyautogui.click(645, 525, duration=0.5)
        pyautogui.write(produto)
#   2-Clicar e digitar quantidade
        pyautogui.click(645, 557, duration=0.5)
        pyautogui.write(quantidade)
#   3-Clicar e digitar preço
        pyautogui.click(645, 595, duration=0.5)
        pyautogui.write(preco)
#   4-Clicar em registrar
        pyautogui.click(493, 792, duration=0.5)
        sleep(1)





