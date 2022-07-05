# Teste de avaliação Engenheiro de Dados 

Este teste busca avaliar quesitos técnicos para engenheiros de dados que almejam trabalhar com os mais diversos projetos de dados por meio de boas práticas. 

## O desafio 

Seu objetivo é calcular preços para grupos de clientes dado suas condições de pagamento iguais, calculando o preço para cada condição de pagamento até a condição máxima do grupo 

Exemplo: Produto com sku 7891022100938 e seu preço base é R$ 10,00 tabela com fator multiplicador condições disponíveis (grupo : fator) 7:0,1, 14:0,15, 21:0,2 e 28:0,25  

- Clientes do grupo de condição 0 devem possuir a seguinte política de preço para esse produto 7891022100938 10,00   

- Clientes do grupo de condição 7 devem possuir a seguinte política de preço para esse produto 7891022100938 10,00 11,00  

- Clientes do grupo de condição 14 devem possuir a seguinte política de preço para esse produto 7891022100938 10,00 11,00 11,5   

- Clientes do grupo de condição 21 devem possuir a seguinte política de preço para esse produto 7891022100938 10,00 11,00 11,5 12,00 

- Clientes do grupo de condição 28 devem possuir a seguinte política de preço para esse produto 7891022100938 10,00 11,00 11,5 12,00 12,5 

O banco de dados SQLite ([loja.db](datasource/loja.db)) e a tabela de condição ([tabela_condicao.csv](datasource/tabela_condicao.csv)) com o grupo:fator se encontram na pasta [datasource](datasource)