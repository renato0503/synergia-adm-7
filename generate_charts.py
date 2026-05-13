import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

# Output directory
out_dir = r"c:\Users\Renato\Documents\Synergia - GP\assets"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

def save_plot(name):
    plt.savefig(os.path.join(out_dir, f"{name}.png"), bbox_inches='tight', dpi=150, transparent=True)
    plt.close()

# GRUPO 2 - TRANSPORTE
# 1. Cobertura
data2_1 = {'Bairro': ['Nobre', 'Centro', 'Periferia A', 'Periferia B'], 'Cobertura (%)': [98, 95, 45, 30]}
df2_1 = pd.DataFrame(data2_1)
plt.figure(figsize=(8, 5))
sns.barplot(data=df2_1, x='Bairro', y='Cobertura (%)', palette='Blues_d')
plt.title('Cobertura de Transporte Público por Região')
save_plot('chart2_1')

# 2. Tempo de Espera
times = [15, 12, 45, 55]
plt.figure(figsize=(8, 5))
plt.bar(['Nobre', 'Centro', 'Periferia A', 'Periferia B'], times, color='#3a7bd5')
plt.ylabel('Minutos')
plt.title('Tempo Médio de Espera (Pico)')
save_plot('chart2_2')

# 3. Pavimentação vs Transporte
x = np.array([10, 30, 50, 70, 90])
y = np.array([5, 15, 45, 80, 95])
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', color='#00d2ff', linewidth=3)
plt.xlabel('% de Pavimentação')
plt.ylabel('Acesso ao Transporte (%)')
plt.title('Correlação Pavimentação x Acessibilidade')
save_plot('chart2_3')

# 4. Orçamento vs Gasto
data2_4 = {'Ano': ['2022', '2023', '2024'], 'Previsto': [10, 12, 15], 'Executado': [4, 5, 3]}
df2_4 = pd.DataFrame(data2_4)
df2_4.plot(x='Ano', kind='bar', stacked=False, color=['#94a3b8', '#00d2ff'])
plt.title('Execução Orçamentária (Milhões R$)')
save_plot('chart2_4')

# 5. Satisfação
plt.figure(figsize=(6, 6))
plt.pie([10, 20, 70], labels=['Bom', 'Regular', 'Ruim'], autopct='%1.1f%%', colors=['#10b981', '#f59e0b', '#ef4444'])
plt.title('Nível de Satisfação do Usuário Periférico')
save_plot('chart2_5')


# GRUPO 4 - DADOS
# 1. Subnotificação
plt.figure(figsize=(8, 5))
sns.lineplot(x=['2020', '2021', '2022', '2023', '2024'], y=[90, 85, 88, 82, 80], marker='s', color='#f59e0b')
plt.title('Índice de Dados Desatualizados (%)')
save_plot('chart4_1')

# 2. Arrecadação Perdida
plt.figure(figsize=(8, 5))
plt.bar(['IPTU', 'ISS', 'Taxas'], [500, 300, 150], color='#fbbf24')
plt.title('Arrecadação Potencial Perdida (K R$)')
save_plot('chart4_2')

# 3. Demandas Atendidas
labels = ['Atendidas', 'Ignoradas']
sizes = [15, 85]
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#10b981', '#ef4444'], startangle=140)
plt.title('Demandas da Comunidade no Sistema')
save_plot('chart4_3')

# 4. Erro de Cadastro
plt.figure(figsize=(8, 5))
sns.boxplot(data=[[10, 12, 15], [40, 55, 60]], palette='YlOrBr')
plt.xticks([0, 1], ['Centro', 'Periferia'])
plt.title('Margem de Erro Cadastral (%)')
save_plot('chart4_4')

# 5. TI Investimento
plt.figure(figsize=(8, 5))
plt.stackplot(['Jan', 'Fev', 'Mar', 'Abr'], [10, 20, 15, 30], labels=['Infra', 'Software'], colors=['#f59e0b', '#fbbf24'])
plt.title('Investimento em Modernização (R$)')
save_plot('chart4_5')


# GRUPO 6 - SANEAMENTO
# 1. Doenças
plt.figure(figsize=(8, 5))
plt.plot(['2022', '2023', '2024'], [300, 320, 350], 'ro--', linewidth=2)
plt.title('Casos de Doenças de Veiculação Hídrica')
save_plot('chart6_1')

# 2. Rede de Esgoto
data6_2 = {'Cidade': ['Curitiba', 'S. Paulo', 'Cuiabá (Geral)', 'Cuiabá (Perif)'], 'Rede (%)': [99, 92, 60, 5]}
df6_2 = pd.DataFrame(data6_2)
sns.barplot(data=df6_2, x='Cidade', y='Rede (%)', palette='Greens_r')
plt.xticks(rotation=15)
plt.title('Comparativo de Rede de Esgoto')
save_plot('chart6_2')

# 3. Gasto Saúde vs Saneamento
plt.figure(figsize=(8, 5))
plt.scatter([1, 2, 3, 4], [10, 8, 6, 4], s=100, color='#10b981')
plt.xlabel('Investimento Saneamento')
plt.ylabel('Gasto Saúde Pública')
plt.title('Correlação: + Saneamento = - Gasto Saúde')
save_plot('chart6_3')

# 4. Destinação Verba
plt.figure(figsize=(6, 6))
plt.pie([70, 20, 10], labels=['Áreas Nobres', 'Manutenção', 'Periferia'], colors=['#94a3b8', '#3a7bd5', '#10b981'])
plt.title('Destinação Real da Verba Federal')
save_plot('chart6_4')

# 5. Índice de Balneabilidade
plt.figure(figsize=(8, 5))
sns.heatmap(np.random.rand(4, 4), cmap='RdYlGn', annot=True)
plt.title('Índice de Contaminação por Quadrante')
save_plot('chart6_5')

print("Charts generated successfully.")
