import sqlite3 
import pandas as pd
import numpy as np

con = sqlite3.connect('datasource/loja.db')

cliente_df = pd.read_sql_query('SELECT codigo, nome_razao_social, condicao FROM cliente', con)
produto_df = pd.read_sql_query('SELECT sku, preco FROM produto', con)

cliente_df.rename(columns={'codigo': 'cod_cliente'}, inplace=True)
produto_df.rename(columns={'preco': 'preco_condicao_0'}, inplace=True)

tabela_condicoes = pd.read_csv('datasource/tabela_condicao.csv').sort_values(by=['condicao'])
# transforma o dataframe em um dicionario para facilitar a busca
dict_condicoes = tabela_condicoes.set_index('condicao').T.to_dict()

tabela_preco_condicao = pd.DataFrame(columns=['cod_cliente', 'sku', 'nome_razao_social', 'condicao', 'preco_condicao_0'])

def calcula_preco_condicao_fator(condicao_cliente: int, condicao_atual: int, preco_base: float):
    if condicao_cliente in dict_condicoes and condicao_atual <= condicao_cliente:
            return preco_base * (1 + dict_condicoes[condicao_atual]['fator'])
    else:
      return np.nan

def cria_novo_registro(cod_produto, cod_cliente, condicoes):
    new_row = pd.DataFrame({'cod_cliente': cod_cliente, 'sku': cod_produto}, index=[0])
    new_row['nome_razao_social'] = cliente_df['nome_razao_social'][cliente_df['cod_cliente'] == cod_cliente].values[0]
    new_row['condicao'] = cliente_df['condicao'][cliente_df['cod_cliente'] == cod_cliente].values[0]
    new_row['preco_condicao_0'] = produto_df['preco_condicao_0'][produto_df['sku'] == cod_produto].values[0]
    preco_base = new_row['preco_condicao_0']
    condicao_cliente = new_row['condicao']
    for index, row in condicoes.iterrows():
        new_row['preco_condicao_'+str(int(row['condicao']))] = calcula_preco_condicao_fator(condicao_cliente.values[0], row['condicao'], preco_base.values[0])
    return new_row
    

continuar = 's'
while continuar == 's':
    try:
        cod_produto = input("Digite o código do produto (sku): ") # or '7898632210323' valor default caso branco
        cod_cliente = input("Digite o código do cliente: ") # or '10505' valor default caso branco
        novo_registro = cria_novo_registro(cod_produto, cod_cliente, tabela_condicoes)
    except IndexError:
        print("Erro ao ler os dados. Verifique se os digitou corretamente.")
        continuar = input("Deseja tentar novamente? (s/n): ")
        continue
    
    tabela_preco_condicao = tabela_preco_condicao.append(novo_registro, ignore_index=True)
    
    print(tabela_preco_condicao)

    continuar = input("Deseja inserir outro registro? (s/n): ")
    if continuar == 'n':
        persistir = input("Deseja persistir os dados no banco? (s/n): ")
        if persistir == 's':
            # salva tabela_preco_condicao no banco de dados
            tabela_preco_condicao.to_sql('preco_condicao_pedido', con, if_exists='append', index=False)
            print("Dados persistidos no banco de dados.")
            input("Pressione Enter para sair.")
            con.close()
        else:
            print("Dados não persistidos.")
            input("Pressione Enter para sair.")
            con.close()
            



