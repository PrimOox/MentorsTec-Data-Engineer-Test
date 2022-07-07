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

---
## Execução do projeto

Caso queira testar apenas o executável do projeto sem baixar o código fonte, baixe o arquivo zip que contém o executável com a base de dados [neste link](https://github.com/PrimOox/MentorsTec-Data-Engineer-Test/releases).  
Ou se desejar executar com o código fonte, siga os passos em diante:  
Utilizando uma IDE de sua preferência, faça o clone do projeto com o seguinte comando: 
```
git clone https://github.com/PrimOox/MentorsTec-Data-Engineer-Test
```

Instale os pacotes necessários, localizado no arquivo [requirements.txt](requirements.txt) com o comando abaixo:
```
pip install -r requirements.txt  
```

Execute o arquivo [main.py](main.py) no console e forneça os dados solicitados.
```
python main.py
```

Você pode visualizar os dados com um SGBD de sua preferência.  
Sugestões: [sqlitebrowser](https://sqlitebrowser.org/dl/), [SQLite Manager (extensão do chrome)](https://chrome.google.com/webstore/detail/sqlite-manager/njognipnngillknkhikjecpnbkefclfe?hl=pt).