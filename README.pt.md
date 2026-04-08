# Career-Ops

[English](README.md) | [Português](README.pt.md)

<p align="center">
  <a href="https://github.com/Wancoe/career-ops-template"><img src="docs/career-ops-banner.png" alt="Career-Ops — Ferramenta de carreira" width="800"></a>
</p>

Career-Ops é uma coleção de ferramentas locais para gerenciar a busca por emprego: avaliar vagas, gerar currículos em PDF personalizados, escanear portais de emprego e controlar o pipeline de candidaturas.

## O que é Career-Ops?

Career-Ops é um toolkit independente orientado a repositório que ajuda você a:

- Avaliar ofertas de trabalho com um método estruturado
- Criar PDFs personalizados a partir de templates HTML
- Escanear vagas com consultas configuráveis
- Acompanhar candidaturas e avaliações em Markdown
- Executar workflows em lote e verificar a integridade dos dados

Esta versão é mantida em `Wancoe/career-ops-template` e não depende de plataformas de agente externas.

## Funcionalidades

- **Avaliação de vagas** com estrutura em blocos
- **Geração de PDF** a partir de `templates/cv-template.html`
- **Scanner de portais** com `templates/portals.example.yml`
- **Gestão de tracker** com scripts de merge, dedup e validação
- **Processos em lote** para avaliações em massa
- **Dashboard opcional** em terminal com Go
- **Local-first**: seus dados ficam na máquina e no repositório

## Início rápido

```bash
# Clone o repositório
git clone https://github.com/Wancoe/career-ops-template.git
cd career-ops-template
npm install
npx playwright install chromium

# Configure o projeto
cp config/profile.example.yml config/profile.yml
cp templates/portals.example.yml portals.yml

# Crie seus arquivos
# - cv.md: seu currículo em Markdown
# - article-digest.md: projetos e métricas opcionais

# Verifique o setup
npm run doctor
```

## Uso básico

Use os scripts e guias do repositório para trabalhar no processo de busca de emprego.

### Avaliar vagas
- Leia `modes/oferta.md` para orientação de avaliação
- Adicione relatórios em `reports/`
- Controle pontuações e status em `data/applications.md`

### Gerar PDF de currículo
- Personalize `templates/cv-template.html`
- Execute:

```bash
node generate-pdf.mjs /tmp/cv-custom.html output/cv-custom-2026-04-08.pdf --format=a4
```

### Gerenciar o tracker

```bash
node merge-tracker.mjs
node normalize-statuses.mjs
node dedup-tracker.mjs
node verify-pipeline.mjs
```

### Escanear portais

Edite `portals.yml` com suas empresas e consultas alvo.

## Documentação

- Guia CLI completo: [`CLI_GUIDE_PT.md`](CLI_GUIDE_PT.md)
- Referência rápida: [`QUICK_REFERENCE_PT.md`](QUICK_REFERENCE_PT.md)
- Guia simples PT-BR: [`GUIA_SIMPLES_PT.md`](GUIA_SIMPLES_PT.md)

## Estrutura do projeto

```
career-ops/
├── config/
├── data/
├── dashboard/
├── docs/
├── examples/
├── jds/
├── modes/
├── output/
├── reports/
├── templates/
└── batch/
```

## Aviso

Career-Ops é uma ferramenta local, não um serviço hospedado.

- Seus dados ficam no repositório e na sua máquina.
- Use portais de emprego conforme os termos de serviço.
- Avaliações são recomendações, não garantias.

Consulte [LEGAL_DISCLAIMER.md](LEGAL_DISCLAIMER.md) para mais detalhes.

## Licença

MIT
