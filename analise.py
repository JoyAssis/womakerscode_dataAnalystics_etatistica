import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Carregando o dataset
dados = pd.read_json('enem_2023.json') 

# Verificando as primeiras linhas do dataset
print(dados.head())

# Verificando as informações do dataset
#print(dados.info())

# Verificando a quantidade de valores nulos
# print(dados.isnull().sum())

# Verificando a quantidade de valores únicos
#print(dados.nunique())

#1 Qual disciplina tem maior amplitude?
# amplitude = dados.drop(columns=['Sexo']).max() - dados.drop(columns=['Sexo']).min()
# materia_maior_amplitude = amplitude.idxmax()
# maior_amplitude = amplitude.max()

# print(f"A disciplina com maior amplitude de notas é {materia_maior_amplitude} com uma amplitude de {maior_amplitude:.2f}")

#Qual média e mediana de cada disciplina?
media_mediana = dados.drop(columns=['Sexo']).agg(['mean', 'median']) #agg é uma função que permite aplicar várias funções de uma vez, nesse caso, média e mediana para cada disciplina (coluna) do dataset. A mean e a median são funções que já ignoram os valores nulos por padrão.

print("Média e mediana de cada disciplina:")
print(media_mediana)

#3 Qual o desvio padrão das notas dos 500 estudantes mais bem colocados de acordo com a os critérios de pesos da Universidade Federal de Pernambuco (UFPE)?
# O desvio padrão é uma medida de dispersão que indica o quanto os valores estão afastados da média. Quanto maior o desvio padrão, maior a dispersão dos valores.
# Para calcular o desvio padrão dos 500 estudantes mais bem colocados, é preciso organizar o dataset de acordo com a nota final e pegar as 500 primeiras linhas, definir os pesos e calcular o desvio padrão das notas desses 500 estudantes.

dados = dados.dropna(subset=['Redação','Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da natureza']) #removendo os valores nulos

print(dados.isnull().sum())
# # definindo os pesos
pesos = {'Redação': 2, 'Matemática': 4, 'Linguagens': 2, 'Ciências humanas': 1, 'Ciências da natureza': 1}

# calculando a nota final ponderada
dados['Nota final'] = (dados['Redação']*pesos['Redação'] + dados['Matemática']*pesos['Matemática'] + dados['Linguagens']*pesos['Linguagens'] + dados['Ciências humanas']*pesos['Ciências humanas'] + dados['Ciências da natureza']*pesos['Ciências da natureza'])/sum(pesos.values())

# ordenando o dataset de acordo com a nota final
top_500 = dados.sort_values(by='Nota final', ascending=False).head(500)

# calculando o desvio padrão das notas dos 500 estudantes mais bem colocados
media_top_500 = top_500['Nota final'].mean()
desvio_padrao_top_500 = top_500['Nota final'].std()

# Exibir os resultados
print(f"Média das notas dos 500 melhores colocados: {media_top_500:.2f}")
print(f"Desvio padrão das notas dos 500 melhores colocados: {desvio_padrao_top_500:.2f}")

#Se todos os  500 estudantes apelicassem para CIE, mas existem apenas 40 vagas, qual a variância e a media das notas dos estudantes que entraram no curso?

top_40 = top_500.head(40) #pegando os 40 primeiros estudantes
media_top_40 = top_40['Nota final'].mean() #calculando a média das notas dos 40 estudantes
variancia_top_40 = top_40['Nota final'].var() #calculando a variância das notas dos 40 estudantes

print(f"Média das notas dos 40 estudantes que entraram no curso: {media_top_40:.2f}")
print(f"Variância das notas dos 40 estudantes que entraram no curso: {variancia_top_40:.2f}")

#extra: nota de corte
nota_corte = top_40['Nota final'].min() #pegando a nota do 40º estudante
print(f"Nota de corte: {nota_corte:.2f}")

#boxplot dos 40 que entraram
plt.figure(figsize=(8,6))
plt.boxplot(top_40['Nota final'], vert=True, patch_artist=True)

plt.title('Boxplot das notas dos 40 estudantes que entraram no curso')
plt.ylabel('Nota final', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() #exibindo o boxplot (local boxplot-top40.png)

# Calcular o terceiro quartil (Q3) para Matemática e Linguagens
q3_matematica = dados['Matemática'].quantile(0.75)
q3_linguagens = dados['Linguagens'].quantile(0.75)

# Exibir os resultados
q3_matematica, q3_linguagens
