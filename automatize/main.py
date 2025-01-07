import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o firefox e entrar no googledrive

pyautogui.press('win')
pyautogui.write('firefox')
pyautogui.press('enter') 
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.press('enter')

# voltar para a area de trabalho
pyautogui.hotkey('win', 'd')
# cliquei no arquivo que eu quero e arrastei ele
pyautogui.moveTo(x=1851, y=54)
pyautogui.mouseDown()
pyautogui.moveTo(x=1014, y=771)
# enquanto eu to arrastando, vou mudar para o firefox
pyautogui.hotkey('alt', 'tab')
# largar o arquivo no google drive
pyautogui.mouseUp()

# esperar 5 segundos
time.sleep(3)

pyautogui.alert("O código acabou de rodar.")