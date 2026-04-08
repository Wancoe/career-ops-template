# Career-Ops

[English](README.md) | [Português](README.pt.md)

<p align="center">
  <a href="https://github.com/Wancoe/career-ops-template"><img src="docs/hero-banner.jpg" alt="Career-Ops — Career management toolkit" width="800"></a>
</p>

<p align="center">
  Career-Ops is a local career workflow toolkit for evaluating jobs, generating tailored CV PDFs, scanning job boards, and tracking applications through terminal scripts and markdown files.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white" alt="Node.js">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white" alt="Go">
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT">
  <br>
  <img src="https://img.shields.io/badge/EN-blue?style=flat" alt="EN">
  <img src="https://img.shields.io/badge/PT--BR-green?style=flat" alt="PT-BR">
</p>

---

## What is Career-Ops?

Career-Ops is a standalone repository for managing a career search workflow. It helps you:

- Evaluate job opportunities with structured scoring
- Create tailored CV PDFs from HTML templates
- Scan configured job portals and collect job links
- Track applications and evaluation notes in Markdown
- Run batch workflows and integrity checks locally

This version is maintained independently in `Wancoe/career-ops-template` and is intended for local use without needing an external hosted service.

## Features

- **Job evaluation** using a structured multi-block framework
- **PDF generation** from `templates/cv-template.html`
- **Portal scanning** driven by `templates/portals.example.yml`
- **Tracker management** with merge, dedup, and validation scripts
- **Batch workflows** for local report processing
- **Dashboard support** with a Go-based terminal UI
- **Local-first**: all workflow data stays in your repository

## Quick start

```bash
# Clone the repository
git clone https://github.com/Wancoe/career-ops-template.git
cd career-ops-template
npm install
npx playwright install chromium

# Configure the project
cp config/profile.example.yml config/profile.yml
cp templates/portals.example.yml portals.yml

# Create your files
# - cv.md: your resume in Markdown
# - article-digest.md: optional project and metrics notes

# Verify setup
npm run doctor
```

## Basic usage

Use the repository scripts and guides to manage evaluations, PDF generation, and tracking.

### Evaluate jobs
- Read `modes/oferta.md` for evaluation guidance
- Add reports in `reports/`
- Track scores and status in `data/applications.md`

### Generate tailored PDFs
- Customize `templates/cv-template.html`
- Run:

```bash
node generate-pdf.mjs /tmp/cv-custom.html output/cv-custom-2026-04-08.pdf --format=a4
```

### Manage the tracker

```bash
node merge-tracker.mjs
node normalize-statuses.mjs
node dedup-tracker.mjs
node verify-pipeline.mjs
```

### Scan portals

Edit `portals.yml` with your target companies and search queries.

## Documentation

- Full CLI guide: [`CLI_GUIDE.md`](CLI_GUIDE.md)
- Quick reference: [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md)
- Portuguese CLI guide: [`CLI_GUIDE_PT.md`](CLI_GUIDE_PT.md)
- PT-BR quick guide: [`GUIA_SIMPLES_PT.md`](GUIA_SIMPLES_PT.md)

## Project structure

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

## Disclaimer

Career-Ops is a local tool, not a hosted service.

- Your data stays on your machine and in your repository.
- Use job portals according to their terms of service.
- Evaluations are guidance, not guarantees.

See [LEGAL_DISCLAIMER.md](LEGAL_DISCLAIMER.md) for full details.

## License

MIT
