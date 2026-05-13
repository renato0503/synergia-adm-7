# Mapas Interativos Synergia - QGIS Web

Este repositório contém três módulos de mapas interativos desenvolvidos para o projeto Synergia (UNIFACC Cuiabá), focados na análise geoespacial de infraestrutura e serviços públicos na Região Metropolitana de Cuiabá.

## 📁 Estrutura de Arquivos

- `mapa_grupo2.html`: Focado em **Transporte Público e Mobilidade**.
- `mapa_grupo4.html`: Focado em **Invisibilidade de Dados e Georreferenciamento**.
- `mapa_grupo6.html`: Focado em **Saneamento Básico e Saúde Ambiental**.

## 🚀 Funcionalidades Estilo QGIS

Todos os mapas incluem:
- **Alternância de Camadas (Layers)**: Controle total sobre o que é exibido no mapa.
- **Painel Lateral de KPIs**: Indicadores em tempo real baseados nos dados plotados.
- **Ferramentas de Medição**: Meça distâncias e áreas diretamente no navegador (Leaflet.draw).
- **Exportação**: Botão para facilitar a captura da vista atual.
- **Base Cartográfica Dupla**: Opção entre mapa de ruas (OSM) e imagens de satélite (Esri).

## 🛠️ Personalização de Dados

Os dados estão estruturados como objetos GeoJSON/JavaScript embutidos no final de cada arquivo HTML. Para atualizar com dados reais:
1. Localize a constante `const data = { ... }`.
2. Substitua as coordenadas e propriedades pelas extraídas de ferramentas como QGIS ou Google Earth.
3. Formatos suportados: `Point`, `LineString`, `Polygon`.

## 📦 Dependências
As bibliotecas são carregadas via CDN para garantir portabilidade:
- Leaflet.js
- Leaflet.draw (Medição)
- Leaflet.markercluster (Agrupamento de pontos)

---
**Orientação:** Prof. Renato Rosa
**Instituição:** UNIFACC Cuiabá - Administração e Gestão Pública
