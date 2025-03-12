import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mode


# Carregando o dataset
dados = pd.read_json('enem_2023.json') 

# Verificando as primeiras linhas do dataset
print(dados.head())

dados = dados.dropna(subset=['Redação','Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da natureza']) #removendo os valores nulos

print(dados.isnull().sum())

# 6 Criando histogramas para Redação e Linguagens com intervalos de 20 pontos
# plt.figure(figsize=(12, 5))

# # Histograma de Redação
# plt.subplot(1, 2, 1)
# plt.hist(dados['Redação'], bins=range(0, 1001, 20), color='blue', alpha=0.7, edgecolor='black')
# plt.title('Histograma de Redação')
# plt.xlabel('Nota')
# plt.ylabel('Frequência')

# # Histograma de Linguagens
# plt.subplot(1, 2, 2)
# plt.hist(dados['Linguagens'], bins=range(0, 1001, 20), color='green', alpha=0.7, edgecolor='black')
# plt.title('Histograma de Linguagens')
# plt.xlabel('Nota')

# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(12, 5))

# 7 Histograma de Redação com range fixo
# plt.subplot(1, 2, 1)
# plt.hist(dados['Redação'], bins=50, range=[0, 1000], color='blue', alpha=0.7, edgecolor='black')
# plt.title('Histograma de Redação (0 a 1000)')
# plt.xlabel('Nota')
# plt.ylabel('Frequência')

# # Histograma de Linguagens com range fixo
# plt.subplot(1, 2, 2)
# plt.hist(dados['Linguagens'], bins=50, range=[0, 1000], color='green', alpha=0.7, edgecolor='black')
# plt.title('Histograma de Linguagens (0 a 1000)')
# plt.xlabel('Nota')

# plt.tight_layout()
# plt.show()

# 8 Criando boxplots
# plt.figure(figsize=(8, 6))
# plt.boxplot([dados['Ciências da natureza'], dados['Redação']], labels=['Ciências da Natureza', 'Redação'], patch_artist=True)

# plt.title("Boxplot das Notas de Ciências da Natureza e Redação")
# plt.ylabel("Nota")
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

# Identificando outliers pelo método IQR
def encontrar_outliers(coluna):
    Q1 = np.percentile(dados[coluna].dropna(), 25)
    Q3 = np.percentile(dados[coluna].dropna(), 75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    outliers = dados[(dados[coluna] < lim_inf) | (dados[coluna] > lim_sup)]
    return outliers

outliers_natureza = encontrar_outliers('Ciências da natureza')
outliers_redacao = encontrar_outliers('Redação')

print(f"Outliers em Ciências da Natureza: {len(outliers_natureza)}")
print(f"Outliers em Redação: {len(outliers_redacao)}")

print("Outliers em Ciências da Natureza:")
print(outliers_natureza)

print("\nOutliers em Redação:")
print(outliers_redacao)

# Recalcular os limites para verificar se há erro
Q1_natureza = np.percentile(dados['Ciências da natureza'].dropna(), 25)
Q3_natureza = np.percentile(dados['Ciências da natureza'].dropna(), 75)
IQR_natureza = Q3_natureza - Q1_natureza
lim_inf_natureza = Q1_natureza - 1.5 * IQR_natureza
lim_sup_natureza = Q3_natureza + 1.5 * IQR_natureza

Q1_redacao = np.percentile(dados['Redação'].dropna(), 25)
Q3_redacao = np.percentile(dados['Redação'].dropna(), 75)
IQR_redacao = Q3_redacao - Q1_redacao
lim_inf_redacao = Q1_redacao - 1.5 * IQR_redacao
lim_sup_redacao = Q3_redacao + 1.5 * IQR_redacao

print(f"Limites para Ciências da Natureza: Inferior={lim_inf_natureza:.2f}, Superior={lim_sup_natureza:.2f}")
print(f"Limites para Redação: Inferior={lim_inf_redacao:.2f}, Superior={lim_sup_redacao:.2f}")

# 9 Dataframes sem os outliers
dados_sem_outliers = dados.copy()

for coluna in ['Ciências da natureza', 'Redação']:
    Q1 = np.percentile(dados[coluna].dropna(), 25)
    Q3 = np.percentile(dados[coluna].dropna(), 75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    dados_sem_outliers = dados_sem_outliers[(dados_sem_outliers[coluna] >= lim_inf) & (dados_sem_outliers[coluna] <= lim_sup)]

# 10 Comparando a média antes e depois
media_original = dados[['Ciências da natureza', 'Redação']].mean().mean()
media_sem_outliers = dados_sem_outliers[['Ciências da natureza', 'Redação']].mean().mean()

# Verificando a alteração em porcentagem
diferenca = abs(media_original - media_sem_outliers) / media_original * 100

print(f"Média original: {media_original:.2f}")
print(f"Média sem outliers: {media_sem_outliers:.2f}")
print(f"Alteração na média: {diferenca:.2f}%")

if diferenca > 5:
    print("A remoção dos outliers alterou significativamente a média (acima de 5%).")
else:
    print("A remoção dos outliers não alterou significativamente a média.")

# Criar cópias do dataset com valores nulos substituídos
colunas_numericas = dados.select_dtypes(include=['number']).columns

dados_media = dados.copy()
dados_mediana = dados.copy()
dados_moda = dados.copy()

dados_media[colunas_numericas] = dados[colunas_numericas].fillna(dados[colunas_numericas].mean())
dados_mediana[colunas_numericas] = dados[colunas_numericas].fillna(dados[colunas_numericas].median())
dados_moda[colunas_numericas] = dados[colunas_numericas].fillna(dados[colunas_numericas].mode().iloc[0])  # Pega a primeira moda encontrada

# Calcular médias e desvios padrões antes e depois
media_original = dados[colunas_numericas].mean()
desvio_original = dados[colunas_numericas].std()

media_media = dados_media[colunas_numericas].mean()
desvio_media = dados_media[colunas_numericas].std()

media_mediana = dados_mediana[colunas_numericas].mean()
desvio_mediana = dados_mediana[colunas_numericas].std()

media_moda = dados_moda[colunas_numericas].mean()
desvio_moda = dados_moda[colunas_numericas].std()

# Comparação das alterações
dif_media = abs(media_original - media_media).mean()
dif_mediana = abs(media_original - media_mediana).mean()
dif_moda = abs(media_original - media_moda).mean()

# Verificar qual medida afeta menos
melhor_medida = min([('Média', dif_media), ('Mediana', dif_mediana), ('Moda', dif_moda)], key=lambda x: x[1])[0]

print(f"Alteração média ao usar Média: {dif_media:.2f}")
print(f"Alteração média ao usar Mediana: {dif_mediana:.2f}")
print(f"Alteração média ao usar Moda: {dif_moda:.2f}")

print(f"A melhor medida para substituir os valores nulos é: {melhor_medida}")