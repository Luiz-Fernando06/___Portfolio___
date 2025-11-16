#Analise de dados e automação dos dados:
# Tarefas a se realizar:
'''
 -Importa a base de dados - FEITO

 -Visualizar a base de dados(analise exploratoria) - FEITA

 -Faturamento por loja - FEITO

 -Quantidade de produtos vendidos por loja - FEITA

 -Ticket medio por produto de cada loja - FEITO

 -Enviar essa analise por e-mail automaticamente - FEITO
 '''

#Bibliotecas necessarias: Pandas, Openpyxl, Pywin32

import pandas as pd
#import openpyxl - como o arquivo e excel então foi necessario instalar essa biblioteca, mas não preciso importa-la
import smtplib
from email.message import EmailMessage

df = pd.read_excel("Vendas (1).xlsx")
pd.set_option('display.max_columns', None) #Amostra todas as minhas colunas
print('Vizualizando as 5 primeiras linhas', df.head())
print('Linhas e Colunas: ',df.shape)
print('Informações gerais: ', df.info())
print('Verificando valores nulos: ', df.isnull().sum())

'''Tabelas de dados sem valores nulos, com 100999 linhas e 7 colunas , com os tipos de dados das colunas certo, sem
necessidade de conversão, pronta para filtragem de dados'''

print('-'*50)

#Calculando o faturamento
Faturamento_loja = df[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(Faturamento_loja)

print('-'*50)

#Calculando quantidades vendidas de lojas
Qetd_vendida_loja = df[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(Qetd_vendida_loja)

print('-'*50)

#Calculando o tickt medio
ticketMedio_Produto_Loja = (Faturamento_loja['Valor Final'] / Qetd_vendida_loja['Quantidade']).to_frame() #Transforma em tabela
ticketMedio_Produto_Loja = ticketMedio_Produto_Loja.rename(columns={0: 'Ticket Médio'})
print(ticketMedio_Produto_Loja)

#Enviando email:
remetente = 'SEU E-MAIL'
destinatario = 'E-MAIL DO DESTINATARIO'
assunto = 'Relatorio de vendas por loja'
html_content = f"""
<p>Prezados,</p>
<p>Segue o relatório de vendas por cada loja.</p>

<p>Faturamento:</p>
{Faturamento_loja.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{Qetd_vendida_loja.to_html()}

<p>Ticket Médio:</p>
{ticketMedio_Produto_Loja.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Att,<br>Luiz Fernando</p>
"""

senha = 'SENHA DO SEU APP'

msg = EmailMessage()
msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = assunto

msg.add_alternative(html_content, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
    email.login(remetente, senha)
    email.send_message(msg)

print('\nArquivo enviado com sucesso')






