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

A maior variação de notas foi observada na disciplina Matemática, indicando uma maior dispersão dos resultados dos candidatos.

A nota média dos 500 melhores estudantes foi 557.29, enquanto a média dos 40 aprovados foi 636.68, sugerindo que apenas os candidatos com notas bem acima da média geral conseguiram a aprovação.

A nota mínima para aprovação foi de 619.21.

A análise dos boxplots indicou a presença de outliers nas disciplinas de Ciências da Natureza e Redação. O método IQR identificou 2 outliers em Ciências da Natureza e 1 em Redação.

A remoção dos outliers teve impacto mínimo (0.06% de alteração na média).
→ Isso significa que os outliers não estavam distorcendo significativamente os dados.

A substituição de valores nulos por média, mediana ou moda teve impacto 0.00% na média geral.
→ Todas as medidas resultaram praticamente no mesmo valor médio após a substituição.

O critério de escolha foi o menor impacto na distribuição.
→ Como todas as medidas tiveram impacto quase zero, o critério usado foi que a média é geralmente a melhor opção quando os dados estão bem distribuídos e não têm assimetria extrema.

Por que a média foi a melhor escolha?
Os dados são simétricos ou aproximadamente normais

Como vimos nos histogramas, as distribuições de notas não são extremamente assimétricas.
Em distribuições simétricas, a média é o melhor estimador porque representa bem o "centro" dos dados.
A moda pode não representar bem os dados

A moda depende da frequência dos valores e pode não ser representativa se houver muitos valores únicos.
No ENEM, por exemplo, poucas pessoas têm exatamente a mesma nota, então a moda pode não ser um bom substituto.
A mediana é útil em distribuições muito assimétricas

A mediana é uma boa escolha se houvesse valores extremos, mas como a remoção dos outliers não alterou significativamente a média, isso sugere que os dados não têm uma assimetria muito grande.

📌 Conclusão
✔️ Como os dados não foram muito afetados pela remoção de outliers, isso indica que não há grandes distorções na distribuição.
✔️ Todas as medidas (média, mediana e moda) tiveram impacto praticamente nulo na alteração da média geral.
✔️ A média foi escolhida porque é um bom estimador central quando os dados são aproximadamente normais e bem distribuídos.

📢 Contribuição

Sugestões e melhorias são bem-vindas! Feel free to fork, criar PRs ou abrir issues. 🚀
