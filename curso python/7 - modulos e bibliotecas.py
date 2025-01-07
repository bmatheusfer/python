import os # biblioteca pastas/arquivos do computador
# import datetime # biblioteca permite trabalhar horas/datas
# import pyautogui # biblioteca para simular controle mouse/teclado
# pandas biblioteca para excel como base de dados
# openpyxl biblioteca para excel para editor

#pyautogui.press("win")
#pyautogui.write("chrome")

# print(os.listdir("arquivos"))
# print(datetime.date.today())

lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    