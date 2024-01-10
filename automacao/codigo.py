import pyautogui
import time
# clicar -> pyautogui.click()//escrever ...write//apertar ...press//scroll ...rolar a pagina

pyautogui.PAUSE = 2 #pausa de 1 segundo
pyautogui.press("win") #aperta a tecla 
pyautogui.write("chrome") #digita a palavra
pyautogui.press("enter") #aperta a tecla enter 

time.sleep(3)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #variavel com o link
pyautogui.write(link) # digita todo o link

pyautogui.press("enter") #aperta a tecla enter
time.sleep(5) #espera 5s
pyautogui.click(x=642, y=409) #clicar na caixa do email dado a sua posiçao
#digitar o email
pyautogui.write("diegop2.@gmail.com")
#passar para o campo de senha
pyautogui.press("tab")
#digitar a senha
pyautogui.write("flamengo100%")
#apertar logar
#pyautogui.click(x=704, y=595)#logando com a posição do botao
pyautogui.press("enter")#logando com o enter

time.sleep(3)

#Importar a base de dados
# pip install pandas numpy openpyxl
import pandas
# seleciona uma coluna,informação da tebela usa o [],excessao do pandas.
tabela = pandas.read_csv("produtos.csv")
#print(tabela)

for linha in tabela.index:    
    # Cadastrar um produto
    pyautogui.click(x=623, y=290) #clicar na caixa do codigo do produto dado a sua posiçao
    # codigo
    codigo = tabela.loc[linha,"codigo"] #passa a linha e a coluna
    pyautogui.write(codigo)
    pyautogui.press("tab") #pula para a proxima caixa
    #marca
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"])) # "1"
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):#verifica se o obs esta vazio,se for falso(nao estiver vazio) executa
        pyautogui.write()
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000) #faz a rolagem da tela para cima