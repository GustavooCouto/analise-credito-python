import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar o dataset
arquivo = 'default_of_credit_card_clients__courseware_version_1_21_19.xls'
df = pd.read_excel(arquivo, header=1)

# Exercício 1: Listas com nomes das características financeiras
bill_features = ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']
pay_features = ['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

# Exercício 2: Estatísticas descritivas das faturas
print("Resumo das faturas (bill features):")
print(df[bill_features].describe())

# Exercício 3: Histograma das faturas (2x3)
plt.figure(figsize=(12, 8))
for i, feature in enumerate(bill_features):
    plt.subplot(2, 3, i+1)
    df[feature].hist(bins=20)
    plt.title(feature)
plt.tight_layout()
plt.show()

# Exercício 4: Estatísticas descritivas dos pagamentos
print("Resumo dos pagamentos (pay features):")
print(df[pay_features].describe())

# Exercício 5: Histograma dos pagamentos (2x3) com rotação no eixo x
plt.figure(figsize=(12, 8))
for i, feature in enumerate(pay_features):
    plt.subplot(2, 3, i+1)
    df[feature].hist(bins=20)
    plt.title(feature)
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Exercício 6: Contar pagamentos iguais a 0
pagamentos_zeros = (df[pay_features] == 0).sum()
print("Pagamentos iguais a zero:")
print(pagamentos_zeros)

# Exercício 7: Histograma logarítmico para valores de pagamento > 0
df_pagamentos_positivos = df[pay_features].replace(0, np.nan).dropna()

log_df = df_pagamentos_positivos.apply(np.log10)

plt.figure(figsize=(12, 8))
for i, feature in enumerate(pay_features):
    plt.subplot(2, 3, i+1)
    log_df[feature].hist(bins=20)
    plt.title(f'log10({feature})')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
