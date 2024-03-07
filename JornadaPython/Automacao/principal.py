import pyautogui #biblioteca para manipulação do teclado
import pandas as pd #biblioteca para manipulação de tabelas
import time #biblioteca para tempo

#Delay de 1 segundo para cada comando que será feito com pyautogui
pyautogui.PAUSE = 1

#Entrar no site da empresa - link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Abrir o firefox
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

#colocar o link do site - Se demorar muito para o firefox abrir o texto digitado pode não aparecer
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Fazer o login
#Duas maneiras: 1 - Encontrando a posição a ser clicada; 2 - Usando TAB
pyautogui.press("TAB")
pyautogui.write("joaozin@gmail.com")
pyautogui.press("TAB")
pyautogui.write("senhajoaozinho")
pyautogui.press("TAB")
pyautogui.press("enter")

#Importar os produtos da base .csv
tabela = pd.read_csv("produtos.csv")
print(tabela)

#Cadastrar todos os produtos percorrendo a tabela como uma matriz
pyautogui.press("TAB")
colunas = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]
for linha in tabela.index:
    for i in range(7):
        valor = tabela.loc[linha, colunas[i]]
        if not pd.isna(valor):
            pyautogui.write(str(valor))
        pyautogui.press("TAB")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=673, y=229)

