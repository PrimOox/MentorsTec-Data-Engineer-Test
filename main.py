import sqlite3 
import pandas as pd
import numpy as np

con = sqlite3.connect('datasource/loja.db')
tabelas_db_loja = pd.read_sql_query('''SELECT name FROM  sqlite_master 
                        WHERE type ='table' AND name NOT LIKE 'sqlite_%';''', con)


cliente_df = pd.read_sql_query('SELECT * FROM cliente', con)
produto_df = pd.read_sql_query('SELECT * FROM produto', con)

cliente_df.drop(['index', 'data_cadastro', 'situacao', 'email', 'classificacao_cliente', 'ramo_atividade'], axis=1, inplace=True)
cliente_df.rename(columns={'codigo': 'cod_cliente'}, inplace=True)

produto_df.drop(['index', 'descricao', 'familia', 'data_lancamento', 'origem', 'unidade_medida'], axis=1, inplace=True)
produto_df.rename(columns={'preco': 'preco_condicao_0'}, inplace=True)

tabela_condicoes = pd.read_csv('datasource/tabela_condicao.csv').sort_values(by=['condicao'])
# Criar um dicionário da tabela de condições sendo a condição como chave e o fator como valor, pois a busca no dicionário é mais rápida
dict_condicoes = tabela_condicoes.set_index('condicao').T.to_dict()


tabela_preco_condicao = pd.DataFrame(columns=['cod_cliente', 'sku', 'nome_razao_social', 'condicao', 'preco_condicao_0'])

def define_preco_condicao_fator(condicao_cliente: int, condicao_atual: int, preco_base: float):
    if condicao_cliente in dict_condicoes and condicao_atual <= condicao_cliente:
            return preco_base * (1 + dict_condicoes[condicao_atual]['fator'])
    else:
      return np.nan

def calcula_precos(cod_produto, cod_cliente, condicoes):
    new_row = pd.Series({'cod_cliente': cod_cliente, 'sku': cod_produto})
    new_row['nome_razao_social'] = cliente_df['nome_razao_social'][cliente_df['cod_cliente'] == cod_cliente].values[0]
    new_row['condicao'] = cliente_df['condicao'][cliente_df['cod_cliente'] == cod_cliente].values[0]
    new_row['preco_condicao_0'] = produto_df['preco_condicao_0'][produto_df['sku'] == cod_produto].values[0]
    preco_base = new_row['preco_condicao_0']
    condicao_cliente = new_row['condicao']
    for index, row in condicoes.iterrows():
        new_row['preco_condicao_'+str(int(row['condicao']))] = define_preco_condicao_fator(condicao_cliente, row['condicao'], preco_base)
    return new_row
    
def concatena_tabela_preco_condicao(tabela, registro):
    tabela = tabela.append(registro, ignore_index=True)
    return tabela    


continuar = 's'
while continuar == 's':
    cod_produto = input("Digite o código (sku) do produto: ") or '7898632210323' # valor default caso branco
    cod_cliente = input("Digite o código do cliente: ") or '10505' # valor default caso branco
    
    serie = calcula_precos(cod_produto, cod_cliente, tabela_condicoes)
    novo_registro = pd.concat([serie, tabela_preco_condicao.reset_index(drop=True, inplace=True)], axis=1, ignore_index=True).T

    tabela_preco_condicao = concatena_tabela_preco_condicao(tabela_preco_condicao, novo_registro)
    
    print(tabela_preco_condicao)

    continuar = input("Deseja continuar? (s/n): ")



