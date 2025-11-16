# Web Scraping Automatizado de Imóveis — Martinelli Imobiliária

## Objetivo:
Automatizar a coleta diária de informações de imóveis disponíveis para venda no site da Imobiliária Martinelli, registrando preços, links e data de coleta em uma planilha Excel.

## Principais etapas realizadas:

- Acesso automatizado: Utilização do Selenium WebDriver (com webdriver-manager) para abrir o site e navegar de forma controlada pelo script.

- Extração de dados: Captura automática dos preços e links de cada anúncio de imóvel na página.

- Registro temporal: Inclusão da data de coleta para acompanhamento histórico de preços e anúncios.

- Armazenamento estruturado: Criação e atualização automática do arquivo imoveis.xlsx, garantindo persistência e organização dos dados.

- Execução contínua: O processo pode ser agendado para rodar periodicamente, permitindo análise de variações de preços e monitoramento do mercado imobiliário local.

## Resumo:
Automação desenvolvida em Python + Selenium + OpenPyXL, voltada para coleta e registro inteligente de dados imobiliários, ideal para análise de mercado, acompanhamento de tendências e atualização de preços em tempo real.
