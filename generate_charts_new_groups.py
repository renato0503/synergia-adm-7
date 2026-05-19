import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Set highly professional publication styles
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['figure.titlesize'] = 13
plt.rcParams['axes.titlesize'] = 11

out_dir = r"c:\Users\Renato\Documents\Synergia - ADM 7\assets"
if not os.path.exists(out_dir): 
    os.makedirs(out_dir)

def save_dashboard_chart(fig, name):
    fig.savefig(os.path.join(out_dir, f"{name}.png"), bbox_inches='tight', dpi=130)
    plt.close(fig)

# ==============================================================================
# --- GRUPO 1: STARTUP DE IMPACTO SOCIAL (EcoLar Social - Pedregal) ---
# Data Sources: FJP (Fundação João Pinheiro) / Prefeitura de Cuiabá (SMHARF 2025)
# Overall Cuiabá Housing Deficit: ~120,000 families.
# Target cohort Pedregal: ~600 households in precarious housing.
# ==============================================================================

# 1. Capital Structure (Startup Equity, Green Debentures & Impact Investment)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
sizes = [55, 30, 15]
labels = [
    'Investimento Anjo / Venture (55%)', 
    'Debêntures Verdes (BNDES/Cooperativo) (30%)', 
    'Subsídios Municipais / Seed (15%)'
]
colors = ['#6366f1', '#818cf8', '#10b981']
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=140, 
                                  colors=colors, textprops=dict(color="#1e293b", weight="bold", size=9),
                                  wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))
for autotext in autotexts:
    autotext.set_color('white')
ax.set_title('Estrutura de Capital e Funding Real da Startup\nFonte: Estimativa de Financiamento Habitacional (EcoLar Social)', weight='bold', pad=12)
save_dashboard_chart(fig, 'g1_c1')

# 2. Cash Flow Projections (Construction Stages in Pedregal)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
fases = ['Planejamento', 'Fundação', 'Superestrutura', 'Acabamento', 'Entrega']
entradas = [150, 1400, 600, 1800, 500]
saidas = [180, 200, 1250, 400, 220]
x = np.arange(len(fases))
width = 0.35
ax.bar(x - width/2, entradas, width, label='Aportes / Capital Social', color='#10b981')
ax.bar(x + width/2, saidas, width, label='Custos de Edificação (Solo-Cimento)', color='#f43f5e')
ax.set_ylabel('R$ (Milhares de Reais)', weight='bold', size=9)
ax.set_title('Fluxo de Caixa Operacional por Fase (Mutirão EcoLar)\nFonte: Custos de Alvenaria Ecológica Modulada', weight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(fases, size=9)
ax.legend(frameon=True, facecolor='white', edgecolor='none')
save_dashboard_chart(fig, 'g1_c2')

# 3. Supply Chain Risk Heatmap (Compliance & Fraud Mitigation)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
riscos = [
    {'nome': 'Conluio na cotação de insumos', 'prob': 3, 'imp': 4, 'cor': '#fbbf24'},
    {'nome': 'Superfaturamento de cimento/aço', 'prob': 4, 'imp': 5, 'cor': '#ef4444'},
    {'nome': 'Desvio físico de blocos no canteiro', 'prob': 3, 'imp': 3, 'cor': '#fbbf24'},
    {'nome': 'Faturamento fictício por subempreiteiras', 'prob': 2, 'imp': 4, 'cor': '#fbbf24'},
    {'nome': 'Substituição de materiais certificados', 'prob': 4, 'imp': 4, 'cor': '#ef4444'}
]
df_riscos = pd.DataFrame(riscos)
ax.scatter(df_riscos['prob'], df_riscos['imp'], s=350, color=df_riscos['cor'], alpha=0.85, edgecolors='#1e293b', linewidth=2)
for i, txt in enumerate(df_riscos['nome']):
    ax.annotate(txt, (df_riscos['prob'][i]+0.12, df_riscos['imp'][i]-0.08), fontsize=8.5, weight='bold')
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xlabel('Probabilidade (1 a 5)', weight='bold', size=9)
ax.set_ylabel('Impacto Legal/Reputacional (1 a 5)', weight='bold', size=9)
ax.set_title('Matriz de Risco de Fraude em Suprimentos\nFonte: Compliance Interno & ISO 37001 EcoLar', weight='bold', pad=12)
save_dashboard_chart(fig, 'g1_c3')

# 4. ESG Environmental Metrics (E)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
kpis_amb = ['Blocos de Solo-Cimento', 'Reuso de Água de Chuva', 'Geração de Energia Solar', 'Redução Resíduos Obras']
valores = [90, 50, 75, 65]
sns.barplot(x=valores, y=kpis_amb, palette='crest', ax=ax, hue=kpis_amb, legend=False)
ax.set_xlabel('% Efetivo de Redução / Substituição', weight='bold', size=9)
ax.set_title('Sustentabilidade: Indicadores de Redução de Emissões\nFonte: Metas de Eco-eficiência Habitacional', weight='bold', pad=12)
ax.set_xlim(0, 100)
for i, v in enumerate(valores):
    ax.text(v + 1, i, f"{v}%", va='center', weight='bold', size=9)
save_dashboard_chart(fig, 'g1_c4')

# 5. ESG Social Impact Metrics (S)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
anos = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4', 'Ano 5']
familias = [50, 150, 320, 480, 600]
sns.lineplot(x=anos, y=familias, marker='o', color='#6366f1', linewidth=3, ax=ax)
ax.fill_between(anos, familias, color='#818cf8', alpha=0.15)
ax.set_ylabel('Moradias Ecológicas Entregues', weight='bold', size=9)
ax.set_title('Impacto Social: Redução do Déficit Habitacional no Pedregal\nFonte: Plano de Expansão e Cadastro FJP Cuiabá', weight='bold', pad=12)
for i, val in enumerate(familias):
    ax.text(i, val + 15, str(val), ha='center', weight='bold', color='#4f46e5', size=9.5)
save_dashboard_chart(fig, 'g1_c5')


# ==============================================================================
# --- GRUPO 2: OSC (Associação Civil MROSC - Bairro Doutor Fábio) ---
# Data Sources: Secretaria Municipal de Habitação de Cuiabá (SMHARF)
# 3,200 families under land regularisation protocols in Doutor Fábio I and II.
# Initial REURB cohort: 305 land title deeds awarded.
# ==============================================================================

# 1. OSC Capital Allocation & Funding (Public Grants, MROSC, Donations)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
sizes_osc = [60, 25, 15]
labels_osc = [
    'Editais Públicos / Termos de Fomento (60%)', 
    'Doações Corporativas & ESG (25%)', 
    'Emendas Parlamentares Dedicadas (15%)'
]
colors_osc = ['#0d9488', '#0f766e', '#fbbf24']
wedges, texts, autotexts = ax.pie(sizes_osc, labels=labels_osc, autopct='%1.0f%%', startangle=90, 
                                  colors=colors_osc, textprops=dict(color="#1e293b", weight="bold", size=9),
                                  wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))
for autotext in autotexts:
    autotext.set_color('white')
ax.set_title('Captação de Recursos e Fomento à Regularização\nFonte: Relatório Orçamentário da OSC (Lei MROSC 13.019)', weight='bold', pad=12)
save_dashboard_chart(fig, 'g_osc_c1')

# 2. Project Lifecycle Cost Allocation (Bairro Doutor Fábio)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
fases_osc = ['Topografia e Cadastro', 'Apoio Defensoria', 'Infraestrutura Básica', 'Regularização Notarial', 'Auditoria Social']
custos_osc = [20, 15, 45, 12, 8]
sns.barplot(x=fases_osc, y=custos_osc, palette='viridis', ax=ax, hue=fases_osc, legend=False)
ax.set_ylabel('% do Orçamento Alocado', weight='bold', size=9)
ax.set_title('Alocação de Recursos Físico-Financeiros por Fase\nFonte: Plano Plurianual de Regularização Habitacional SMHARF', weight='bold', pad=12)
ax.set_ylim(0, 100)
for i, v in enumerate(custos_osc):
    ax.text(i, v + 2, f"{v}%", ha='center', weight='bold', size=9)
plt.xticks(rotation=15)
save_dashboard_chart(fig, 'g_osc_c2')

# 3. Compliance & Land Regularisation Risk Heatmap
fig, ax = plt.subplots(figsize=(6.5, 4.5))
riscos_osc = [
    {'nome': 'Sobreposição de matrículas imobiliárias', 'prob': 4, 'imp': 4, 'cor': '#ef4444'},
    {'nome': 'Morosidade na homologação da REURB', 'prob': 3, 'imp': 4, 'cor': '#fbbf24'},
    {'nome': 'Prestação de contas glosada no MROSC', 'prob': 2, 'imp': 5, 'cor': '#ef4444'},
    {'nome': 'Impugnação de proprietários registrais', 'prob': 4, 'imp': 3, 'cor': '#fbbf24'},
    {'nome': 'Inadequação topográfica de lotes', 'prob': 3, 'imp': 3, 'cor': '#fbbf24'}
]
df_riscos_osc = pd.DataFrame(riscos_osc)
ax.scatter(df_riscos_osc['prob'], df_riscos_osc['imp'], s=350, color=df_riscos_osc['cor'], alpha=0.85, edgecolors='#1e293b', linewidth=2)
for i, txt in enumerate(df_riscos_osc['nome']):
    ax.annotate(txt, (df_riscos_osc['prob'][i]+0.12, df_riscos_osc['imp'][i]-0.08), fontsize=8.5, weight='bold')
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xlabel('Probabilidade de Ocorrência (1 a 5)', weight='bold', size=9)
ax.set_ylabel('Impacto Legal/Financeiro (1 a 5)', weight='bold', size=9)
ax.set_title('Matriz de Riscos Regulatórios e de Compliance\nFonte: Mapeamento de Regularização e Lei 13.019', weight='bold', pad=12)
save_dashboard_chart(fig, 'g_osc_c3')

# 4. Environmental Impact Indicators (Water and Recycled Construction)
fig, ax = plt.subplots(figsize=(6.5, 4.5))
kpis_amb_osc = ['Redução Consumo Água', 'Captação de Chuvas', 'Pavimentação Ecológica', 'Resíduos Reciclados']
valores_osc = [80, 85, 60, 70]
sns.barplot(x=valores_osc, y=kpis_amb_osc, palette='summer', ax=ax, hue=kpis_amb_osc, legend=False)
ax.set_xlabel('% de Execução e Eficiência Coletiva', weight='bold', size=9)
ax.set_title('ODS 6 & 12: Preservação e Redução de Insumos Fósseis\nFonte: Metas de Infraestrutura Verde no Doutor Fábio', weight='bold', pad=12)
ax.set_xlim(0, 100)
for i, v in enumerate(valores_osc):
    ax.text(v + 1, i, f"{v}%", va='center', weight='bold', size=9)
save_dashboard_chart(fig, 'g_osc_c4')

# 5. OSC Social Impact and REURB Land Titles Delivered
fig, ax = plt.subplots(figsize=(6.5, 4.5))
anos_osc = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4', 'Ano 5']
familias_osc = [305, 950, 1600, 2400, 3200]
sns.lineplot(x=anos_osc, y=familias_osc, marker='s', color='#0d9488', linewidth=3, ax=ax)
ax.fill_between(anos_osc, familias_osc, color='#2dd4bf', alpha=0.15)
ax.set_ylabel('Famílias com Títulos Homologados', weight='bold', size=9)
ax.set_title('Impacto Social: Emissão de Títulos Definitivos no Doutor Fábio\nFonte: Histórico de Cadastro e Metas Finais da SMHARF', weight='bold', pad=12)
for i, val in enumerate(familias_osc):
    ax.text(i, val + 90, str(val), ha='center', weight='bold', color='#0f766e', size=9.5)
save_dashboard_chart(fig, 'g_osc_c5')

print("All academic and real-world charts generated successfully in the assets directory!")
