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
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.labelsize'] = 11.5
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

out_dir = r"c:\Users\Renato\Documents\Synergia - ADM 7\assets"
if not os.path.exists(out_dir): 
    os.makedirs(out_dir)

def save_dashboard_chart(fig, name):
    # Ensure layout fits perfectly and does not truncate text
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, f"{name}.png"), bbox_inches='tight', dpi=180)
    plt.close(fig)

# ==============================================================================
# --- GRUPO 1: STARTUP DE IMPACTO SOCIAL (EcoLar Social - Pedregal) ---
# ==============================================================================

# 1. Capital Structure (Startup Equity, Green Debentures & Impact Investment)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
sizes = [55, 30, 15]
labels = [
    'Investimento Anjo / Venture (55%)', 
    'Debêntures Verdes (BNDES) (30%)', 
    'Subsídios Municipais / Seed (15%)'
]
colors = ['#4f46e5', '#3b82f6', '#10b981'] # Vibrant indigo, blue, emerald
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=140, 
                                  colors=colors, textprops=dict(color="#0f172a", weight="bold", size=11),
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2.5))
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(12)
    autotext.set_weight('bold')
ax.set_title('1. Estrutura de Capital da Startup EcoLar Social\nFonte: Estudo de Financiamento Habitacional (EcoLar Social 2026)', weight='bold', pad=15, color="#0f172a")
save_dashboard_chart(fig, 'g1_c1')

# 2. Cash Flow Projections (Construction Stages in Pedregal)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
fases = ['Planejamento', 'Fundação', 'Superestrutura', 'Acabamento', 'Entrega']
entradas = [150, 1400, 600, 1800, 500]
saidas = [180, 200, 1250, 400, 220]
x = np.arange(len(fases))
width = 0.35

rects1 = ax.bar(x - width/2, entradas, width, label='Aportes / Capital Social', color='#10b981')
rects2 = ax.bar(x + width/2, saidas, width, label='Custos de Edificação (Solo-Cimento)', color='#e11d48')

ax.set_ylabel('R$ (Milhares de Reais)', weight='bold', size=11, color="#0f172a")
ax.set_title('2. Projeção de Fluxo de Caixa Operacional por Fases\nFonte: Planilha de Custos Unitários de Alvenaria Ecológica', weight='bold', pad=15, color="#0f172a")
ax.set_xticks(x)
ax.set_xticklabels(fases, size=11, color="#0f172a", weight="bold")
ax.legend(frameon=True, facecolor='white', edgecolor='none')

# Add values above bars for clarity
ax.bar_label(rects1, padding=3, weight='bold', size=10, color='#047857')
ax.bar_label(rects2, padding=3, weight='bold', size=10, color='#be123c')

save_dashboard_chart(fig, 'g1_c2')

# 3. Supply Chain Risk Heatmap (Compliance & Fraud Mitigation)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
riscos = [
    {'nome': 'Conluio em Insumos', 'prob': 3, 'imp': 4, 'cor': '#ea580c'}, # Orange
    {'nome': 'Superfaturamento', 'prob': 4, 'imp': 5, 'cor': '#e11d48'}, # Red
    {'nome': 'Desvio de Blocos', 'prob': 3, 'imp': 3, 'cor': '#eab308'}, # Yellow
    {'nome': 'Faturamento Fictício', 'prob': 2, 'imp': 4, 'cor': '#ea580c'}, # Orange
    {'nome': 'Substituição Insumos', 'prob': 4, 'imp': 4, 'cor': '#e11d48'}  # Red
]
df_riscos = pd.DataFrame(riscos)
ax.scatter(df_riscos['prob'], df_riscos['imp'], s=600, color=df_riscos['cor'], alpha=0.95, edgecolors='#0f172a', linewidth=2.5, zorder=3)

for i, txt in enumerate(df_riscos['nome']):
    ax.annotate(txt, (df_riscos['prob'][i]+0.16, df_riscos['imp'][i]-0.06), fontsize=10, weight='bold', color='#0f172a',
                bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec="#cbd5e1", lw=1.5, alpha=0.9), zorder=4)

ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xlabel('Probabilidade de Ocorrência (1 a 5)', weight='bold', size=11, color="#0f172a")
ax.set_ylabel('Impacto Legal/Financeiro (1 a 5)', weight='bold', size=11, color="#0f172a")
ax.set_title('3. Matriz de Riscos de Fraude em Suprimentos\nFonte: Compliance Interno & ISO 37001 EcoLar', weight='bold', pad=15, color="#0f172a")
ax.grid(True, linestyle='--', alpha=0.5)
save_dashboard_chart(fig, 'g1_c3')

# 4. ESG Environmental Metrics (E)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
kpis_amb = ['Blocos de Solo-Cimento', 'Reuso de Água de Chuva', 'Geração de Energia Solar', 'Redução Resíduos Obras']
valores = [90, 50, 75, 65]
bars = ax.barh(kpis_amb, valores, color=['#059669', '#10b981', '#34d399', '#6ee7b7'], edgecolor='white', height=0.6)
ax.set_xlabel('% Efetivo de Redução / Substituição', weight='bold', size=11, color="#0f172a")
ax.set_title('4. Sustentabilidade: Metas ESG - Indicadores Ambientais\nFonte: Pacto Global da ONU e Metas de Eco-eficiência Habitacional 2026', weight='bold', pad=15, color="#0f172a")
ax.set_xlim(0, 100)
ax.set_yticklabels(kpis_amb, weight='bold', size=11, color='#0f172a')
ax.bar_label(bars, padding=5, weight='bold', size=11, color='#047857', fmt='%d%%')
save_dashboard_chart(fig, 'g1_c4')

# 5. ESG Social Impact Metrics (S)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
anos = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4', 'Ano 5']
familias = [50, 150, 320, 480, 600]
ax.plot(anos, familias, marker='o', color='#4f46e5', linewidth=4, markersize=10, markerfacecolor='#4f46e5', markeredgecolor='white', markeredgewidth=2)
ax.fill_between(anos, familias, color='#4f46e5', alpha=0.12)
ax.set_ylabel('Moradias Ecológicas Entregues', weight='bold', size=11, color="#0f172a")
ax.set_title('5. Impacto Social: Famílias de Baixa Renda Beneficiadas no Pedregal\nFonte: Secretaria de Habitação / Deficit Habitacional IBGE', weight='bold', pad=15, color="#0f172a")
ax.set_xticklabels(anos, weight='bold', size=11, color='#0f172a')
for i, val in enumerate(familias):
    ax.text(i, val + 18, str(val), ha='center', weight='bold', color='#312e81', size=11)
save_dashboard_chart(fig, 'g1_c5')


# ==============================================================================
# --- GRUPO 2: OSC (Associação Civil MROSC - Bairro Doutor Fábio) ---
# ==============================================================================

# 1. OSC Capital Allocation & Funding (Public Grants, MROSC, Donations)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
sizes_osc = [60, 25, 15]
labels_osc = [
    'Editais Públicos / Fomento (60%)', 
    'Doações Corporativas & ESG (25%)', 
    'Emendas Parlamentares (15%)'
]
colors_osc = ['#0d9488', '#0f766e', '#ea580c'] # Vibrant teals, orange
wedges, texts, autotexts = ax.pie(sizes_osc, labels=labels_osc, autopct='%1.0f%%', startangle=90, 
                                  colors=colors_osc, textprops=dict(color="#0f172a", weight="bold", size=11),
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2.5))
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(12)
    autotext.set_weight('bold')
ax.set_title('1. Fontes de Captação e Financiamento da OSC\nFonte: Relatório Orçamentário da OSC (Lei MROSC 13.019/14)', weight='bold', pad=15, color="#0f172a")
save_dashboard_chart(fig, 'g_osc_c1')

# 2. Project Lifecycle Cost Allocation (Bairro Doutor Fábio)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
fases_osc = ['Topografia e Cadastro', 'Apoio Defensoria', 'Infraestrutura Básica', 'Regularização Notarial', 'Auditoria Social']
custos_osc = [20, 15, 45, 12, 8]
bars_osc = ax.bar(fases_osc, custos_osc, color=['#0d9488', '#14b8a6', '#0f766e', '#115e59', '#134e4a'], edgecolor='white', width=0.65)
ax.set_ylabel('% do Orçamento Alocado', weight='bold', size=11, color="#0f172a")
ax.set_title('2. Cronograma Físico-Financeiro (Alocação por Fases)\nFonte: Plano Plurianual de Regularização Urbana e Custeio Notarial', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 100)
ax.set_xticklabels(fases_osc, size=10, color="#0f172a", weight="bold")
ax.bar_label(bars_osc, padding=3, weight='bold', size=11, color='#0f766e', fmt='%d%%')
save_dashboard_chart(fig, 'g_osc_c2')

# 3. Compliance & Land Regularisation Risk Heatmap
fig, ax = plt.subplots(figsize=(7.5, 5.2))
riscos_osc = [
    {'nome': 'Sobreposição de Matrículas', 'prob': 4, 'imp': 4, 'cor': '#e11d48'}, # Red
    {'nome': 'Morosidade Homologação', 'prob': 3, 'imp': 4, 'cor': '#ea580c'}, # Orange
    {'nome': 'Contas Glosadas (MROSC)', 'prob': 2, 'imp': 5, 'cor': '#e11d48'}, # Red
    {'nome': 'Impugnação de Proprietários', 'prob': 4, 'imp': 3, 'cor': '#ea580c'}, # Orange
    {'nome': 'Inadequação Topográfica', 'prob': 3, 'imp': 3, 'cor': '#eab308'} # Yellow
]
df_riscos_osc = pd.DataFrame(riscos_osc)
ax.scatter(df_riscos_osc['prob'], df_riscos_osc['imp'], s=600, color=df_riscos_osc['cor'], alpha=0.95, edgecolors='#0f172a', linewidth=2.5, zorder=3)

for i, txt in enumerate(df_riscos_osc['nome']):
    ax.annotate(txt, (df_riscos_osc['prob'][i]+0.16, df_riscos_osc['imp'][i]-0.06), fontsize=10, weight='bold', color='#0f172a',
                bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec="#cbd5e1", lw=1.5, alpha=0.9), zorder=4)

ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xlabel('Probabilidade de Ocorrência (1 a 5)', weight='bold', size=11, color="#0f172a")
ax.set_ylabel('Impacto Legal/Financeiro (1 a 5)', weight='bold', size=11, color="#0f172a")
ax.set_title('3. Matriz de Riscos Regulatórios e de Compliance\nFonte: Matriz de Compliance Habitacional e Lei Federal 13.465', weight='bold', pad=15, color="#0f172a")
ax.grid(True, linestyle='--', alpha=0.5)
save_dashboard_chart(fig, 'g_osc_c3')

# 4. Environmental Impact Indicators (Water and Recycled Construction)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
kpis_amb_osc = ['Redução Consumo Água', 'Captação de Chuvas', 'Pavimentação Ecológica', 'Resíduos Reciclados']
valores_osc = [80, 85, 60, 70]
bars_osc_h = ax.barh(kpis_amb_osc, valores_osc, color=['#0f766e', '#0d9488', '#14b8a6', '#2dd4bf'], edgecolor='white', height=0.6)
ax.set_xlabel('% de Execução e Eficiência Coletiva', weight='bold', size=11, color="#0f172a")
ax.set_title('4. Sustentabilidade ODS 6 & 12: Preservação Ambiental\nFonte: Metas de Infraestrutura Verde no Doutor Fábio', weight='bold', pad=15, color="#0f172a")
ax.set_xlim(0, 100)
ax.set_yticklabels(kpis_amb_osc, weight='bold', size=11, color='#0f172a')
ax.bar_label(bars_osc_h, padding=5, weight='bold', size=11, color='#0f766e', fmt='%d%%')
save_dashboard_chart(fig, 'g_osc_c4')

# 5. OSC Social Impact and REURB Land Titles Delivered
fig, ax = plt.subplots(figsize=(7.5, 5.2))
anos_osc = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4', 'Ano 5']
familias_osc = [305, 950, 1600, 2400, 3200]
ax.plot(anos_osc, familias_osc, marker='s', color='#0d9488', linewidth=4, markersize=10, markerfacecolor='#0d9488', markeredgecolor='white', markeredgewidth=2)
ax.fill_between(anos_osc, familias_osc, color='#2dd4bf', alpha=0.12)
ax.set_ylabel('Famílias com Títulos Homologados', weight='bold', size=11, color="#0f172a")
ax.set_title('5. Impacto Social: Emissão de Títulos Definitivos de REURB-S\nFonte: Histórico de Cadastro e Metas Finais da SMHARF Cuiabá', weight='bold', pad=15, color="#0f172a")
ax.set_xticklabels(anos_osc, weight='bold', size=11, color='#0f172a')
for i, val in enumerate(familias_osc):
    ax.text(i, val + 100, str(val), ha='center', weight='bold', color='#115e59', size=11)
save_dashboard_chart(fig, 'g_osc_c5')

print("All academic and real-world charts generated successfully in the assets directory!")
