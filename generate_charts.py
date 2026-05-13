import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Professional Dashboard Style
sns.set_theme(style="white")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

out_dir = r"c:\Users\Renato\Documents\Synergia - GP\assets"
if not os.path.exists(out_dir): os.makedirs(out_dir)

def save_dashboard_chart(fig, name):
    fig.savefig(os.path.join(out_dir, f"{name}.png"), bbox_inches='tight', dpi=120)
    plt.close(fig)

# --- GRUPO 2: TRANSPORTE ---
# 1. Frota
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x=['2020','2021','2022','2023','2024'], y=[250, 280, 310, 350, 385], color='#2563eb', ax=ax)
ax.set_title('Evolução da Frota Operacional')
save_dashboard_chart(fig, 'g2_c1')

# 2. Reclamações
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(x=['Jan','Fev','Mar','Abr','Mai'], y=[450, 420, 580, 510, 490], marker='o', color='#ef4444', ax=ax)
ax.set_title('Índice de Reclamações (SAC)')
save_dashboard_chart(fig, 'g2_c2')

# 3. Pavimentação Periférica
fig, ax = plt.subplots(figsize=(6,4))
plt.pie([35, 65], labels=['Pavimentada', 'Não Pavimentada'], autopct='%1.1f%%', colors=['#3b82f6','#cbd5e1'], startangle=90)
plt.title('Vias de Transporte na Periferia')
save_dashboard_chart(fig, 'g2_c3')

# 4. Cumprimento de Horário
fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(data=[[70,72,68,75,80], [40,45,35,50,42]], ax=ax)
ax.set_xticklabels(['Linhas Tronco', 'Linhas Alimentadoras'])
ax.set_title('Pontualidade (%)')
save_dashboard_chart(fig, 'g2_c4')

# 5. Custo por KM
fig, ax = plt.subplots(figsize=(6,4))
plt.stackplot(['2022','2023','2024'], [3.2, 3.5, 3.8], [1.1, 1.2, 1.4], labels=['Combustível','Manutenção'], colors=['#1e293b','#3b82f6'])
plt.title('Custo Operacional por KM (R$)')
save_dashboard_chart(fig, 'g2_c5')


# --- GRUPO 4: DADOS ---
# 1. Gap Cadastro
fig, ax = plt.subplots(figsize=(6,4))
plt.bar(['Oficial', 'Real (IBGE)'], [185, 231], color=['#94a3b8','#f59e0b'])
plt.title('Imóveis Registrados (Milhares)')
save_dashboard_chart(fig, 'g4_c1')

# 2. Arrecadação Perdida
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x=['Norte','Sul','Leste','Oeste'], y=[15, 42, 18, 35], palette='YlOrBr', ax=ax)
plt.title('Inadimplência IPTU por Regional (%)')
save_dashboard_chart(fig, 'g4_c2')

# 3. Solicitações LAI
fig, ax = plt.subplots(figsize=(6,4))
plt.plot([120, 250, 480, 890], marker='s', color='#f59e0b', linewidth=2)
plt.title('Volume de Pedidos via LAI')
save_dashboard_chart(fig, 'g4_c3')

# 4. Dados Digitais
fig, ax = plt.subplots(figsize=(6,4))
plt.pie([20, 80], labels=['Digitalizado', 'Papel/Manual'], autopct='%1.1f%%', colors=['#f59e0b','#e2e8f0'])
plt.title('Nível de Digitalização do Acervo')
save_dashboard_chart(fig, 'g4_c4')

# 5. Tempo de Resposta
fig, ax = plt.subplots(figsize=(6,4))
sns.kdeplot([5, 10, 15, 20, 45, 60], fill=True, color='#f59e0b', ax=ax)
plt.title('Tempo de Resposta Cidadão (Dias)')
save_dashboard_chart(fig, 'g4_c5')


# --- GRUPO 6: SANEAMENTO ---
# 1. Coleta Esgoto
fig, ax = plt.subplots(figsize=(6,4))
plt.bar(['2017','2024'], [35, 82], color=['#cbd5e1','#10b981'])
plt.title('Evolução Coleta Esgoto (%)')
save_dashboard_chart(fig, 'g6_c1')

# 2. Qualidade Água
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(x=['Jan','Mar','Mai','Jul','Set'], y=[99.1, 99.4, 98.9, 99.8, 99.9], color='#10b981', ax=ax)
plt.title('Índice de Potabilidade (%)')
save_dashboard_chart(fig, 'g6_c2')

# 3. Investimento PPP
fig, ax = plt.subplots(figsize=(6,4))
plt.bar(['Privado (PPP)', 'Público'], [1200, 150], color=['#059669','#1e293b'])
plt.title('Investimento Acumulado (Milhões R$)')
save_dashboard_chart(fig, 'g6_c3')

# 4. Perdas Rede
fig, ax = plt.subplots(figsize=(6,4))
plt.pie([35, 65], labels=['Perdas', 'Faturado'], autopct='%1.1f%%', colors=['#ef4444','#10b981'])
plt.title('Perdas de Água na Rede (%)')
save_dashboard_chart(fig, 'g6_c4')

# 5. Internações
fig, ax = plt.subplots(figsize=(6,4))
sns.regplot(x=np.array([1,2,3,4,5]), y=np.array([500, 450, 380, 310, 250]), color='#10b981', ax=ax)
plt.title('Queda de Internações (SUS) x Saneamento')
save_dashboard_chart(fig, 'g6_c5')

print("New specific dashboards generated.")
