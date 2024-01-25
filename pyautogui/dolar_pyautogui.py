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

    # PARTE QUE MOSTRA NA TELA
    valor = pyperclip.paste()
    pyautogui.alert(text=f'o valor atual do dólar é R${valor}', title='Saída', button='OK')

except pyautogui.FailSafeException:
     pyautogui.alert(text='Evite mover o mouse durante a execução do programa', title='Erro', button='OK')
