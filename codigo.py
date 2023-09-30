# pyautogui.click -> click with the mouse
# pyautogui.write -> Write a text
# pyautogui.press -> press the key
# pyautogui.hotkey -> shortcut (key combination)

# Project step by step

import pyautogui
import time

# step 1: Enter the company system
           # https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 0.5

# Open Google Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Wait for the website to load
time.sleep(5)

# Enter the link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Wait for the website to load
time.sleep(5)

# Step 2: Log in
# Select the access field
pyautogui.click(x=563, y=548)
pyautogui.write("usuario")
pyautogui.press("tab")

pyautogui.write("senha")
pyautogui.press("tab")

pyautogui.press("enter")

# Step 3: Import the product database
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela) 

for linha in tabela.index:
    # Step 4: Register 1 product - # Step 5: Repeat registration for all products in the table
    pyautogui.click(x=531, y=369) # Select first field to fill in

    codigo = tabela.loc[linha, "codigo"]

    # fill in the fields
    pyautogui.write(str(codigo)) 
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"])) 
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"])) 
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"])) 
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) 
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"])) 
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # Press to send
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)
    









