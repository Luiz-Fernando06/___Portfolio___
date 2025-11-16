# Bibliotecas necessarias:
# Abrir a página
from selenium import webdriver
# Seleciona todos os elementos especificos que eu quero
from selenium.webdriver.common.by import By
# Indica aonde ta o chromedrive
from selenium.webdriver.chrome.service import Service
# baixa automaticamente a versão correta do chrome
from webdriver_manager.chrome import ChromeDriverManager
# Pega data atual
from datetime import datetime
# abre arquivo excel
import openpyxl
# lida com os Caminhos e diretorios
import os

# Caminho do Excel (vai salvar na mesma pasta do executável)
arquivo_excel = os.path.join(os.getcwd(), "imoveis.xlsx")

# Se a planilha não existir, cria uma nova
if not os.path.exists(arquivo_excel):
    planilha_imoveis = openpyxl.Workbook()
    pagina_imoveis = planilha_imoveis.active
    pagina_imoveis.title = "precos"
    pagina_imoveis.append(["Preço", "Link", "Data"])
    planilha_imoveis.save(arquivo_excel)

# Abre a planilha existente
planilha_imoveis = openpyxl.load_workbook(arquivo_excel)
pagina_imoveis = planilha_imoveis["precos"]

# Abre o navegador (webdriver-manager cuida da versão do driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1 entrar: https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=129&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4
driver = webdriver.Chrome()
driver.get("https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=129&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4")

# 2 inserir preço, link da casa, data dentro de uma planilha que eu criei
# 3 anotar os preços, links das casas e datas de cada um dos anuncios daquela página
precos = driver.find_elements(By.XPATH, "//div[@class='card-valores']/div")
links = driver.find_elements(By.XPATH, "//a[@class='carousel-cell']")

for preco, link in zip(precos, links):
    preco_limpo = preco.text.strip(' ')
    link_pronto = link.get_attribute('href')
    data_atual = datetime.now().strftime('%d/%m/%Y')
    pagina_imoveis.append([preco_limpo, link_pronto, data_atual])

planilha_imoveis.save(arquivo_excel)

# Fecha o navegador
driver.quit()

print("Coleta finalizada! Os dados foram salvos em imoveis.xlsx")
