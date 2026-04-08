# Career-Ops

[English](README.md) | [Português](README.pt.md)

<p align="center">
  <a href="https://x.com/santifer"><img src="docs/hero-banner.jpg" alt="Career-Ops — Multi-Agent Job Search System" width="800"></a>
</p>

Career-Ops é um conjunto de ferramentas open source para avaliar ofertas de emprego, gerar currículos em PDF personalizados, escanear vagas e gerenciar o pipeline de candidaturas.

## O que ele faz

- Avalia ofertas com uma metodologia estruturada em blocos
- Gera CVs em PDF com palavras-chave e layout profissional
- Escaneia portais e vagas com consultas pré-configuradas
- Gerencia o pipeline de candidaturas em Markdown e TSV

## Como começar

1. Instale Node.js 18+.
2. Execute `npx playwright install chromium`.
3. Copie `config/profile.example.yml` para `config/profile.yml` e edite com seus dados.
4. Copie `templates/portals.example.yml` para `portals.yml`.
5. Use os comandos `node doctor.mjs`, `node merge-tracker.mjs` e `node normalize-statuses.mjs` para verificar o setup.

## Documentação

- Guia completo de terminal: [`CLI_GUIDE_PT.md`](CLI_GUIDE_PT.md)
- Referência rápida: [`QUICK_REFERENCE_PT.md`](QUICK_REFERENCE_PT.md)
- Guia simples em PT-BR: [`GUIA_SIMPLES_PT.md`](GUIA_SIMPLES_PT.md)

## Nota

Este repositório mantém apenas os idiomas inglês e português (PT-BR). A documentação em espanhol, alemão e francês foi removida para simplificar o fluxo.
