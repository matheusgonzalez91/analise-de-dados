import pandas as pd
import plotly.express as px

#Importar a base de dados
tabela = pd.read_csv('telecom_users.csv')

#Excluindo uma tabela
'''
axis = 0 ---> Linha
axis = 1 ---> Coluna
'''
tabela = tabela.drop('Unnamed: 0', axis=1)

#Tratamento dos dados
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

#Excluindo uma coluna vazia
tabela = tabela.dropna(how='all', axis=1)

#Excluindo uma linha vazia
tabela = tabela.dropna(how='any', axis=0)

#Clientes que cancelaram e que não cancelaram
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

#Análise detalhada
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn', color_discrete_sequence=['blue', 'red'])
    grafico.show()