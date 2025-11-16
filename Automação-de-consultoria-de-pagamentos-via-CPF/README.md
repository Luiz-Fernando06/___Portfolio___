# Automação de Consulta e Atualização de Pagamentos via Selenium

## Objetivo:
Automatizar o processo de verificação de status de pagamento de clientes, consultando informações em um site e atualizando automaticamente uma planilha de fechamento.

## Principais etapas realizadas:

- Leitura dos dados: Extração automática de informações (nome, CPF, valor e vencimento) a partir de uma planilha Excel com os dados dos clientes.

- Automação de consultas: Utilização do Selenium WebDriver para acessar o site de verificação de CPF e consultar o status de cada cliente.

- Identificação de pagamentos:

Se o status for “em dia”, o script captura a data e o método de pagamento (cartão ou boleto).

Caso contrário, marca o cliente como “pendente”.

- Atualização automática: As informações são registradas e salvas em uma planilha de fechamento, consolidando todos os resultados.

- Execução contínua: O processo é repetido automaticamente para todos os registros até o final da planilha.

## Resumo:
Automação desenvolvida em Python + Selenium + OpenPyXL, eliminando a necessidade de verificação manual de pagamentos e garantindo maior eficiência, precisão e economia de tempo nos processos administrativos.
