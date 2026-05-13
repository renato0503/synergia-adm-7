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

### 8. Dashboards e Consolidação BI
- **Pedido**: Implementar dashboards reais de Adm Financeira e BI para cada grupo, contendo pelo menos 5 gráficos e mapa de geolocalização.
- **Ações**: 
    - Regeração de 15 gráficos via Python com foco em Dashboards operacionais.
    - Reformulação das páginas dos grupos com seções de "Dashboard de Gestão Financeira e BI" em destaque.

### 9. Formato de Slides e Conteúdo Ostensivo
- **Pedido**: Transformar as páginas dos grupos em formato de slides (15 banners de mesmo tamanho por grupo), adicionando conteúdo educacional completo sobre OGC, PP e BI, e uma proposta integrada de solução.
- **Ações**: 
    - Implementação de `scroll-snap-type: y mandatory` para garantir o formato de slides verticais.
    - Distribuição de conteúdo acadêmico denso (Conceitos, Problemas, Soluções e Referências) em 15 telas por grupo.
    - Inclusão da **Proposta Integrada de Solução** no contexto do projeto.

### 10. Módulos de Mapas Interativos "QGIS Web" (Último Pedido)
- **Pedido**: Criar mapas profissionais independentes estilo QGIS para cada grupo, com controle de camadas, KPIs, ferramentas de medição e exportação.
- **Ações**:
    - Desenvolvimento de `mapa_grupo2.html`, `mapa_grupo4.html` e `mapa_grupo6.html`.
    - Integração de ferramentas avançadas: Medição de área/distância, layer switcher (Satélite/OSM), legendas dinâmicas e painéis laterais de KPIs.
    - Plotagem de dados GeoJSON embutidos representando rotas, redes de infraestrutura e áreas de déficit.
    - Conexão direta dos mapas com os slides da apresentação principal.

### 11. Redesign Premium da Interface de Apresentação
- **Pedido**: Melhorar significativamente o design dos slides de conteúdo (G2, G4, G6), trazendo imagens de contexto, ícones e fontes de dados.
- **Ações**:
    - Substituição completa da UI por um design *High-End* (semelhante a Pitch Decks profissionais) usando tipografia moderna (*Outfit* e *Playfair Display*).
    - Integração de imagens fotográficas em alta resolução (via Unsplash) utilizando layouts em *Split-Screen*.
    - Substituição de emojis básicos pelo pacote de ícones profissionais **Phosphor Icons**.
    - Implementação de animações fluidas de entrada (`fadeUp` via IntersectionObserver) para revelação progressiva do conteúdo.
    - Documentação explícita de fontes oficiais de dados (IBGE, SNIS, ARSEC, TCE-MT) na base dos slides analíticos.

### 12. Otimização Total para Dispositivos Móveis (Responsividade)
- **Pedido**: Criar a versão mobile perfeita para Android e iOS sem alterar a versão PC, otimizando botões e navegação.
- **Ações**:
    - Reestruturação CSS completa baseada em Media Queries (`@media max-width: 768px/900px`).
    - Conversão de layouts de *Grid/Flexbox-Row* para empilhamento vertical (*Column*), garantindo que gráficos e textos sejam perfeitamente legíveis em telas pequenas.
    - Adaptação dos Mapas QGIS-Web: Criação de um menu de gaveta (Sidebar) retrátil inferior com botão de ação flutuante (FAB ⚙️) para maximizar a visualização cartográfica no celular.
    - Redimensionamento de tipografia e botões de navegação para alvos de toque amigáveis, melhorando a experiência do usuário (UX) em mobile.

### 13. Mapas Choropleth com Polígonos Reais de Bairros
- **Pedido**: Substituir mapas genéricos por mapas profissionais com polígonos reais dos bairros de Cuiabá e Várzea Grande, estilo QGIS Web.
- **Ações**:
    - Implementação de mapas com **polígonos reais** de 15 bairros de Cuiaba + 8 bairros de Várzea Grande.
    - Estilo **Choropleth**: bairros pintados conforme intensidade dos dados (verde→amarelo→vermelho).
    - Legendas dinâmicas no canto inferior direito do mapa.
    - GeoJSON embutido no código JavaScript (sem dependências externas).
    - Popups interativos com dados ao hover/click em cada bairro.

### 14. Layouts Personalizados por Grupo (Sem "Quadradinhos Genéricos")
- **Pedido**: Criar visualizações únicas para cada grupo, evitando repetição de layout.
- **Ações**:

#### 🚌 Grupo 2 - Transporte Público
- Layout limpo com **painel estreito (300px)** focado em rotas e mobilidade.
- Sem cards de KPI genéricos.
- Filtros de camadas: Rotas Ativas, Pontos de Parada, Lacunas de Cobertura, Rotas Propostas.
- Linhas de rotas coloridas por status (🟢 Operacional, 🟡 Parcial, 🔴 Inexistente).
- Marcadores customizados (círculos azuis) para pontos de parada.
- Polígonos vermelhos translúcidos marcando áreas sem cobertura.
- Lista de linhas principais com status visual.

#### 📊 Grupo 4 - Invisibilidade de Dados
- Layout de **Dashboard Analítico** com 4 cards de KPIs.
- **Slider temporal (2020-2026)** que atualiza o progresso no mapa.
- Progress bar mostrando evolução do mapeamento ao longo dos anos.
- Choropleth com polígonos coloridos por % de mapeamento cadastral.
- Tabela de bairros críticos (sem dados georreferenciados).
- Botão "Modo Auditoria" para sobreposição IBGE vs Cadastro Municipal.
- Design premium com hover effects nos cards.

#### 💧 Grupo 6 - Saneamento Básico
- Layout temático com **painel estreito (300px)** focado em infraestrutura.
- Sem cards genéricos - indicadores em lista vertical.
- Rede de água: Linhas azuis (#2196F3) com popups mostrando diâmetro e pressão.
- Rede de esgoto: Linhas marrons (#795548) indicando coleta.
- **Ícones SVG inline**: 💧 para poços/ETAs, 🏭 para estações de tratamento.
- Áreas sem cobertura: Polígonos vermelhos com previsão de atendimento.
- Expansão planejada: Linhas tracejadas verdes.
- Lista de bairros com déficit (percentual de esgotamento).

### 15. Melhorias Técnicas nos Mapas
- **Responsividade**: Em telas <768px, painéis viram barra inferior.
- **Z-index controlado**: Mapa (1), controles (500), painéis (1000), popups (2000).
- **Performance**: GeoJSON embutido, carregamento <3s.
- **Exportação**: Botões para exportar CSV e GeoJSON.
- **Escala gráfica**: Adicionada ao canto inferior esquerdo.
- **Layer Switcher**: Alternância entre OSM e Satélite.

---

## 🛠️ Tecnologias Utilizadas
- **Frontend**: HTML5, CSS3 (Modern Grid/Flexbox), JavaScript (Vanilla).
- **Mapas**: Leaflet.js com tiles OpenStreetMap.
- **Análise de Dados**: Python (Pandas, Matplotlib, Seaborn).
- **Infraestrutura**: Git, GitHub, GitHub Pages.

## 🔗 Links Úteis
- **Repositório**: [github.com/renato0503/synergia-gp](https://github.com/renato0503/synergia-gp)
- **Site ao Vivo**: [renato0503.github.io/synergia-gp](https://renato0503.github.io/synergia-gp/)
