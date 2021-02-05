import pandas as pd
import numpy as np
import datetime


input('1º -- Salve o arquivo com o nome paradrão BatchLogAAAA-MM-DD.xlsx\n'
      '2º -- Coloque na pasta batchlog\n'
      '3º -- Pressione enter\n')
batch = pd.read_excel(f'batchlog/BatchLog{datetime.date.today()}.xlsx')
batch_limpo = batch[['Item Qualifier', 'Quantity', 'Message']]
colunas = ['Item Qualifier', 'Quantity']
batch_limpo2 = pd.DataFrame(columns=colunas)
index = 0
for i, row in batch_limpo.iterrows():
    menssagem1 = 'Bin Qty tem de ser 0 ou superior:  Csla.WORMapper.Internals.CslaHelper.CheckIsValid(BusinessBase businessObject)'
    menssagem2 = 'Bin Qty must be 0 or greater:  Csla.WORMapper.Internals.CslaHelper.CheckIsValid(BusinessBase businessObject)'
    menssagem3 = 'Bin Qty tem de ser 0 ou superior:  Csla.WORMapper.Internals.CslaHelper.CheckIsValid(BusinessBase businessObject)'
    if row['Message'] == menssagem1 or row['Message'] == menssagem2 or row['Message'] == menssagem3:
        batch_limpo2.loc[index, 'Item Qualifier'] = row['Item Qualifier'].replace('/B', '')
        batch_limpo2.loc[index, 'Quantity'] = row['Quantity']
        index = index + 1




batch_limpo2 = batch_limpo2.rename(columns={'Item Qualifier': 'CribBin', 'Quantity': 'BinQuantity'})
batch_limpo2 = batch_limpo2.groupby(['CribBin']).sum()

batch_limpo2.to_csv(f'batchlimp/batchlimp{datetime.date.today()}.csv')
print(f'O arquivo foi salvo na pasta batchlimp com o nome de batchlimp{datetime.date.today()}.csv')