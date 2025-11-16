# SustentaScore — Análise do Impacto da Sustentabilidade no Comportamento do Consumidor Natura

## Descrição do Projeto
O projeto SustentaScore tem como objetivo analisar e quantificar o impacto das ações de sustentabilidade da Natura sobre o comportamento de compra e fidelização de seus clientes. Através de dados de vendas, engajamento em campanhas sustentáveis, participação em programas de reciclagem e consumo de produtos ecológicos, o projeto investiga se a sustentabilidade influencia decisões de compra e lealdade à marca.

## Motivação
A Natura é uma referência mundial em sustentabilidade e inovação em cosméticos. Entender como iniciativas socioambientais afetam o comportamento do consumidor permite à empresa:

- Otimizar campanhas de marketing e engajamento sustentável.

- Direcionar recursos para clientes com maior propensão à recompra.

- Avaliar o retorno financeiro e reputacional de iniciativas ambientais.

## Principais Perguntas Respondidas

- As campanhas de sustentabilidade aumentam o interesse de compra dos clientes?

- Clientes que compram produtos sustentáveis gastam mais que os outros?

- Participar do programa de reciclagem aumenta a probabilidade de recompra?

- Existe relação entre engajamento em ações sustentáveis e fidelidade do cliente?

- Nossas ações sustentáveis atraem clientes de regiões ou perfis específicos?

- É possível medir um índice de impacto sustentável (“SustentaScore”) que preveja vendas e recompra?

## Com

- Linguagem e bibliotecas: Python, Pandas, NumPy, Matplotlib, Seaborn, scikit-learn.

- Análise exploratória de dados: distribuição de clusters de clientes, perfil demográfico, engajamento em campanhas, compras e recompra.

- Análise de correlação: relacionamento entre engajamento sustentável, compras totais, ticket médio e recompra.

- Criação do SustentaScore: índice que combina engajamento em campanhas, produtos sustentáveis comprados e participação em reciclagem para medir impacto sustentável.

- Modelo preditivo: Aleatório

## Princípios

- Clientes mais engajados em ações sustentáveis tendem a comprar mais ao longo do tempo (correlação de 0,73 com valor total de compras).

- A participação em reciclagem aumenta a taxa de recompra em 40% (66% vs. 47%).

- Apesar de comprarem produtos sustentáveis, os clientes não necessariamente gastam mais por transação (ticket médio -0,21).

- O SustentaScore é um indicador eficaz para prever vendas e fidelização, permitindo segmentações automáticas e priorização de investimentos em marketing.


## Impacto para o Negócio
O projeto demonstra que ações de sustentabilidade da Natura:

- Reforçam o vínculo emocional com a marca.

- Geram aumento de vendas ao longo do tempo e fidelização de clientes.

- Permitem otimização de campanhas, focando em clientes com maior probabilidade de recompra, economizando orçamento e aumentando a efetividade.

## Como usar o modelo
O modelo permite inserir dados de um cliente (SustentaScore, engajamento, produtos sustentáveis comprados, ticket médio, valor total de compras, participação em reciclagem, região) e gerar a probabilidade de recompra, classificando clientes em alto ou baixa chance de fidelização.
