# Contexto do Projeto Synergia - UNIFACC Cuiabá

Este documento resume as solicitações do Prof. Renato Rosa e as implementações realizadas para a plataforma de apresentação acadêmica do curso de Administração e Gestão Pública.

## 📋 Solicitações e Evolução do Projeto

### 1. Concepção Inicial
- **Pedido**: Criar uma página única (HTML/JS/CSS) para o evento Synergia, focada no problema "O Abismo entre o CEP e a Cidadania".
- **Ações**: Desenvolvimento de interface premium com Glassmorphism, inclusão dos grupos 2, 4 e 6, e geração de imagem de herói via IA.

### 2. Hospedagem e Publicação
- **Pedido**: Subir para o GitHub e configurar o GitHub Pages no repositório `renato0503/synergia-gp`.
- **Ações**: Inicialização de repositório Git, configuração de origin e deploy automatizado para a web.

### 3. Expansão e Interatividade (8 Banners)
- **Pedido**: Criar pelo menos 8 banners por grupo, integrando as disciplinas de Adm Financeira (BI), Orçamento/Governança (OGC) e Políticas Públicas (PP).
- **Ações**: Implementação de sistema de slides vertical, integração de dashboards interativos (Chart.js) e mapas de georreferenciamento (Leaflet).

### 4. Redesign Premium e Gráficos Python
- **Pedido**: Alterar para tema claro (fundo branco, letra escura), aprofundar para 12 telas por grupo e utilizar Python para gerar gráficos profissionais.
- **Ações**: Criação do script `generate_charts.py`, geração de 15 gráficos acadêmicos via Matplotlib/Seaborn e redesenho total da UI com foco em sofisticação executiva.

### 5. Dados Reais e Georreferenciamento
- **Pedido**: Utilizar dados reais de fontes oficiais, incluir pelo menos 4 tabelas por grupo e realizar georreferenciamento real em Cuiabá.
- **Ações**: Pesquisa de dados no Censo IBGE 2022, SNIS 2024, ARSEC e Trata Brasil. Inclusão de tabelas de KPIs e mapas apontando para bairros como Pedregal, Ribeirão do Lipa e Parque Cuiabá.

### 6. Correções Técnicas
- **Pedido**: Resolver erro de Favicon (404) e avisos de "Tracking Prevention" no navegador.
- **Ações**: Implementação de Favicon inline (SVG) e adição de atributos `integrity` e `crossorigin` nos recursos de CDN.

### 7. Estrutura Multi-Páginas e Temas Específicos
- **Pedido**: Separar a plataforma em um arquivo HTML para cada grupo e aprofundar problemas específicos de OGC e PP.
- **Ações**: Criação de `index.html` (Home), `grupo2.html`, `grupo4.html` e `grupo6.html`. Inclusão de discussões sobre:
    - **Grupo 2**: Falta de transparência ativa, ausência de controle interno, paralisação do ciclo de políticas e falta de participação social.
    - **Grupo 4**: Verba de R$ 4,2M para dados, accountability e aplicação da LAI.
    - **Grupo 6**: Parceria Público-Privada (PPP), LAI e aprovação orçamentária anual.

---

## 🛠️ Tecnologias Utilizadas
- **Frontend**: HTML5, CSS3 (Modern Grid/Flexbox), JavaScript (Vanilla).
- **Mapas**: Leaflet.js com tiles OpenStreetMap.
- **Análise de Dados**: Python (Pandas, Matplotlib, Seaborn).
- **Infraestrutura**: Git, GitHub, GitHub Pages.

## 🔗 Links Úteis
- **Repositório**: [github.com/renato0503/synergia-gp](https://github.com/renato0503/synergia-gp)
- **Site ao Vivo**: [renato0503.github.io/synergia-gp](https://renato0503.github.io/synergia-gp/)
