# 📊 Análise de Desempenho no ENEM 2023

Este repositório contém uma análise exploratória dos dados fictícios do ENEM 2023, com foco na seleção de estudantes para o curso de Ciência da Computação da UFPE. Utilizamos estatística descritiva e visualização de dados para extrair insights sobre as notas.
Um Exercício para o bootcamp Data Analytics da Woomakerscode

### 📌 Objetivos

- Identificar a disciplina com maior variação de notas.  
- Calcular médias e medianas das disciplinas.  
- Selecionar os **500 melhores estudantes** e analisar suas notas.  
- Determinar os **40 aprovados** e calcular a variância e a média das notas.  
- Gerar visualizações, como **boxplots** e **histogramas**, para entender a distribuição das notas.  
- Identificar e remover **outliers** utilizando o método **IQR (Intervalo Interquartílico)** e verificar seu impacto na média geral.

### 📂 Estrutura do Repositório

- `enem_2023.json` - Base de dados fictícia do ENEM 2023.  
- `analise.py` - Código principal contendo as análises gerais.
- `Redacao_linguagens.py` - Código contendo toda a análise referente as disciplinas de Redação, linguagens e ciências da natureza.   
- `README.md` - Instruções sobre o projeto.

### ⚙️ Como Rodar o Projeto

Clone o repositório:
```
git clone https://github.com/JoyAssis/womakerscode_dataAnalystics_etatistica.git

cd enem-analise
```
Instale as dependências:
```
pip install pandas numpy matplotlib
```
Execute a análise:
```
python analise.py
```
### 📊 O que foi feito até agora

🔍 Análises Estatísticas Realizadas

- Cálculo da média e mediana das disciplinas do ENEM.

- Identificação da disciplina com maior amplitude de nota.

- Cálculo da média e do desvio padrão dos 500 melhores candidatos.

- Cálculo da média e da variância das notas dos 40 candidatos aprovados.

### 📊 Visualizações Criadas

- Histogramas de Redação e Linguagens (com intervalos de 20 pontos e um segundo histograma ajustando o range para 0 a 1000).

- Boxplot comparativo de Ciências da Natureza e Redação para identificar padrões na distribuição das notas.

- Detecção e análise de outliers usando o método IQR (Intervalo Interquartílico).

### 📌 Insights Obtidos

📌 A maior variação de notas foi observada na disciplina Matemática, indicando uma maior dispersão dos resultados dos candidatos.

📌 A nota média dos 500 melhores estudantes foi 557.29, enquanto a média dos 40 aprovados foi 636.68, sugerindo que apenas os candidatos com notas bem acima da média geral conseguiram a aprovação.

📌 A nota mínima para aprovação foi identificada em X pontos (a definir pelo código).

📌 A análise dos boxplots indicou a presença de outliers nas disciplinas de Ciências da Natureza e Redação. O método IQR identificou 2 outliers em Ciências da Natureza e 1 em Redação.

📌 A remoção dos outliers será avaliada para entender seu impacto na média geral dos candidatos.

📢 Contribuição

Sugestões e melhorias são bem-vindas! Feel free to fork, criar PRs ou abrir issues. 🚀