import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Professional Dashboard Style
sns.set_theme(style="white")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 12

out_dir = r"c:\Users\Renato\Documents\Synergia - ADM 7\assets"
if not os.path.exists(out_dir): os.makedirs(out_dir)

def save_dashboard_chart(fig, name):
    fig.savefig(os.path.join(out_dir, f"{name}.png"), bbox_inches='tight', dpi=120)
    plt.close(fig)

# --- GRUPO 1: STARTUP DE IMPACTO SOCIAL (Joanna, Cinthia, Leandro e Guilherme) ---
# Theme: Indigo & Mint

# 1. Estrutura de Capital (Donut Chart)
fig, ax = plt.subplots(figsize=(6,4))
sizes = [55, 30, 15]
labels = ['Investimento de Impacto (Equity)', 'Debêntures Verdes (Terceiros)', 'Subsídios / Capital Próprio']
colors = ['#4f46e5', '#818cf8', '#10b981']
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90, 
                                  colors=colors, textprops=dict(color="#1e293b", weight="bold"),
                                  wedgeprops=dict(width=0.4, edgecolor='white'))
for autotext in autotexts:
    autotext.set_color('white')
ax.set_title('Estrutura de Capital da Startup de Impacto', weight='bold', pad=15)
save_dashboard_chart(fig, 'g1_c1')

# 2. Projeção de Fluxo de Caixa / Plano de Negócios (Milhares de R$)
fig, ax = plt.subplots(figsize=(6,4))
fases = ['Planejamento', 'Captação', 'Construção', 'Entrega', 'Operação']
entradas = [50, 1200, 300, 1500, 450]
saidas = [120, 150, 1100, 200, 180]
x = np.arange(len(fases))
width = 0.35
ax.bar(x - width/2, entradas, width, label='Entradas (Aportes/Vendas)', color='#10b981')
ax.bar(x + width/2, saidas, width, label='Saídas (Custos/Obras)', color='#ef4444')
ax.set_ylabel('R$ (Milhares)')
ax.set_title('Projeção de Fluxo de Caixa por Fase', weight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(fases)
ax.legend()
save_dashboard_chart(fig, 'g1_c2')

# 3. Matriz de Risco de Fraude (Compliance)
# Mapeamento de Riscos de Compra de Materiais
fig, ax = plt.subplots(figsize=(6,4))
riscos = [
    {'nome': 'Conluio de Fornecedores', 'prob': 4, 'imp': 4, 'cor': '#ef4444'},
    {'nome': 'Superfaturamento', 'prob': 3, 'imp': 5, 'cor': '#ef4444'},
    {'nome': 'Desvio de Insumos', 'prob': 3, 'imp': 3, 'cor': '#f59e0b'},
    {'nome': 'Faturamento Falso', 'prob': 2, 'imp': 4, 'cor': '#f59e0b'},
    {'nome': 'Substituição por Inferior', 'prob': 4, 'imp': 3, 'cor': '#f59e0b'}
]
df_riscos = pd.DataFrame(riscos)
ax.scatter(df_riscos['prob'], df_riscos['imp'], s=300, color=df_riscos['cor'], alpha=0.8, edgecolors='black')
for i, txt in enumerate(df_riscos['nome']):
    ax.annotate(txt, (df_riscos['prob'][i]+0.15, df_riscos['imp'][i]-0.05), fontsize=9, weight='bold')
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xlabel('Probabilidade (1-5)')
ax.set_ylabel('Impacto Legal/Financeiro (1-5)')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title('Matriz de Riscos de Fraude em Suprimentos', weight='bold', pad=15)
save_dashboard_chart(fig, 'g1_c3')

# 4. KPIs Ambientais ESG (Percentual de Redução de Resíduos e Eficiência)
fig, ax = plt.subplots(figsize=(6,4))
kpis_amb = ['Material Reciclado', 'Reuso de Água', 'Energia Solar', 'Redução Resíduos']
valores = [65, 45, 80, 50]
sns.barplot(x=valores, y=kpis_amb, palette='crest', ax=ax)
ax.set_xlabel('% de Adoção / Redução')
ax.set_title('Metas ESG: Indicadores Ambientais', weight='bold', pad=15)
ax.set_xlim(0, 100)
save_dashboard_chart(fig, 'g1_c4')

# 5. KPIs Sociais ESG (Famílias de Baixa Renda Atendidas)
fig, ax = plt.subplots(figsize=(6,4))
anos = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4', 'Ano 5']
familias = [40, 120, 250, 420, 600]
sns.lineplot(x=anos, y=familias, marker='o', color='#4f46e5', linewidth=2.5, ax=ax)
ax.fill_between(anos, familias, color='#818cf8', alpha=0.2)
ax.set_ylabel('Famílias Atendidas')
ax.set_title('Impacto Social: Famílias Beneficiadas', weight='bold', pad=15)
save_dashboard_chart(fig, 'g1_c5')


# --- GRUPO 2: OSC (André, Aliny, Michely e Everson) ---
# Theme: Teal & Forest Green

# 1. Estrutura de Captação de Recursos (Donut Chart)
fig, ax = plt.subplots(figsize=(6,4))
sizes_osc = [40, 25, 20, 15]
labels_osc = ['Editais Públicos', 'Doações/Filantropia', 'Emendas Parlamentares', 'Parcerias Corporativas']
colors_osc = ['#0d9488', '#0f766e', '#14b8a6', '#2dd4bf']
wedges, texts, autotexts = ax.pie(sizes_osc, labels=labels_osc, autopct='%1.0f%%', startangle=90, 
                                  colors=colors_osc, textprops=dict(color="#1e293b", weight="bold"),
                                  wedgeprops=dict(width=0.4, edgecolor='white'))
for autotext in autotexts:
    autotext.set_color('white')
ax.set_title('Fontes de Captação de Recursos da OSC', weight='bold', pad=15)
save_dashboard_chart(fig, 'g_osc_c1')

# 2. Ciclo de Vida do Projeto Financeiro (Custos por Fase)
fig, ax = plt.subplots(figsize=(6,4))
fases_osc = ['Planejamento', 'Regularização', 'Obras/Infra', 'Trabalho Social', 'Operação']
custos_osc = [15, 10, 55, 12, 8]
sns.barplot(x=fases_osc, y=custos_osc, palette='viridis', ax=ax)
ax.set_ylabel('% do Orçamento Total')
ax.set_title('Distribuição de Recursos por Fase do Projeto', weight='bold', pad=15)
ax.set_ylim(0, 100)
for i, v in enumerate(custos_osc):
    ax.text(i, v + 2, f"{v}%", ha='center', weight='bold')
save_dashboard_chart(fig, 'g_osc_c2')

# 3. Matriz de Risco de Compliance (Fraudes em Materiais)
fig, ax = plt.subplots(figsize=(6,4))
riscos_osc = [
    {'nome': 'Conluio na Cotação', 'prob': 4, 'imp': 4, 'cor': '#ef4444'},
    {'nome': 'Superfaturamento', 'prob': 2, 'imp': 5, 'cor': '#ef4444'},
    {'nome': 'Recebimento de Material Menor', 'prob': 3, 'imp': 4, 'cor': '#ef4444'},
    {'nome': 'Desvio de Insumos da Obra', 'prob': 4, 'imp': 3, 'cor': '#f59e0b'},
    {'nome': 'Uso Indevido de Verba (Desvio)', 'prob': 2, 'imp': 5, 'cor': '#ef4444'}
]
df_riscos_osc = pd.DataFrame(riscos_osc)
ax.scatter(df_riscos_osc['prob'], df_riscos_osc['imp'], s=300, color=df_riscos_osc['cor'], alpha=0.8, edgecolors='black')
for i, txt in enumerate(df_riscos_osc['nome']):
    ax.annotate(txt, (df_riscos_osc['prob'][i]+0.15, df_riscos_osc['imp'][i]-0.05), fontsize=9, weight='bold')
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xlabel('Probabilidade (1-5)')
ax.set_ylabel('Impacto Legal/Financeiro (1-5)')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title('Mapeamento de Riscos de Fraude (Compliance)', weight='bold', pad=15)
save_dashboard_chart(fig, 'g_osc_c3')

# 4. KPIs Ambientais ESG (Sustentabilidade das Obras)
fig, ax = plt.subplots(figsize=(6,4))
kpis_amb_osc = ['Coleta de Chuva', 'Painéis Solares', 'Madeira Certificada', 'Resíduos Reciclados']
valores_osc = [85, 60, 95, 70]
sns.barplot(x=valores_osc, y=kpis_amb_osc, palette='summer', ax=ax)
ax.set_xlabel('% de Implementação')
ax.set_title('Metas de Sustentabilidade Ambiental', weight='bold', pad=15)
ax.set_xlim(0, 100)
save_dashboard_chart(fig, 'g_osc_c4')

# 5. KPIs Sociais ESG (Impacto na Comunidade)
fig, ax = plt.subplots(figsize=(6,4))
anos_osc = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4', 'Ano 5']
familias_osc = [50, 150, 300, 500, 750]
sns.lineplot(x=anos_osc, y=familias_osc, marker='s', color='#0d9488', linewidth=2.5, ax=ax)
ax.fill_between(anos_osc, familias_osc, color='#2dd4bf', alpha=0.2)
ax.set_ylabel('Famílias Beneficiadas')
ax.set_title('Impacto Social: Regularização e Moradia', weight='bold', pad=15)
save_dashboard_chart(fig, 'g_osc_c5')

print("Charts generated successfully!")
