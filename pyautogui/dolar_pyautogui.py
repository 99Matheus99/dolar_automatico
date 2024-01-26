import pyautogui
import pyperclip

pyautogui.PAUSE = 2 # 2 segundos de espera por cada comando

try:
    # PARTE QUE PESQUISA
    pyautogui.press('win')
    pyautogui.write('dolar atual')
    pyautogui.press('enter')
    pyautogui.sleep(2) # tempo maior para esperar a página carregar, nesse caso, será 4 segundos

    # PARTE QUE COPIA
    pyautogui.moveTo(232, 496, 2, pyautogui.easeOutQuad)
    pyautogui.click(clicks=2)
    pyautogui.hotkey('ctrl', 'c')
    valor = pyperclip.paste()

    # PARTE QUE ABRE O EMAIL
    pyautogui.moveTo(360, 56, 2, pyautogui.easeOutQuad)
    pyautogui.click()
    pyautogui.write('https://mail.google.com')
    pyautogui.press('enter')

    # PARTE QUE ESCREVE O EMAIL
    pyautogui.moveTo(82, 203, 2, pyautogui.easeOutQuad)
    pyautogui.click()
    pyautogui.write('thomazrb@gmail.com')
    pyautogui.press('tab', presses=2)
    pyautogui.write('valor atual do dolar')
    pyautogui.press('tab')
    pyautogui.write(f'o valor do dolar nesse momento é R${valor}')
    pyautogui.hotkey('ctrl', 'enter')

except pyautogui.FailSafeException:
     pyautogui.alert(text='Evite mover o mouse durante a execução do programa', title='Erro', button='OK')
