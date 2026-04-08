from pathlib import Path

replacements = {
    'README.md': [
        (
            "## What Is This\n\nCareer-Ops turns any AI coding CLI into a full job search command center. Instead of manually tracking applications in a spreadsheet, you get an AI-powered pipeline that:\n\n- **Evaluates offers** with a structured A-F scoring system (10 weighted dimensions)\n- **Generates tailored PDFs** -- ATS-optimized CVs customized per job description\n- **Scans portals** automatically (Greenhouse, Ashby, Lever, company pages)\n- **Processes in batch** -- evaluate 10+ offers in parallel with sub-agents\n- **Tracks everything** in a single source of truth with integrity checks\n\n> **Important: This is NOT a spray-and-pray tool.** Career-ops is a filter -- it helps you find the few offers worth your time out of hundreds. The system strongly recommends against applying to anything scoring below 4.0/5. Your time is valuable, and so is the recruiter's. Always review before submitting.\n\nCareer-ops is agentic: Claude Code navigates career pages with Playwright, evaluates fit by reasoning about your CV vs the job description (not keyword matching), and adapts your resume per listing.\n\n> **Heads up: the first evaluations won't be great.** The system doesn't know you yet. Feed it context -- your CV, your career story, your proof points, your preferences, what you're good at, what you want to avoid. The more you nurture it, the better it gets. Think of it as onboarding a new recruiter: the first week they need to learn about you, then they become invaluable.\n\nBuilt by someone who used it to evaluate 740+ job offers, generate 100+ tailored CVs, and land a Head of Applied AI role. [Read the full case study](https://santifer.io/career-ops-system).\n\n## Features"
            ,
            "## What Is This\n\nCareer-Ops is a customizable, open-source career toolkit for evaluating job offers, generating tailored PDFs, scanning portals, and tracking applications. It is designed to work manually through terminal scripts and markdown files; external AI assistance is optional but not required.\n\n- **Evaluates offers** with a structured A-F scoring system (10 weighted dimensions)\n- **Generates tailored PDFs** -- ATS-optimized CVs customized per job description\n- **Scans portals** automatically with Playwright and targeted search queries\n- **Processes in batch** with local worker scripts and review workflows\n- **Tracks everything** in a single source of truth with integrity checks\n\n> **Important: This is NOT a spray-and-pray tool.** Career-Ops is a filter -- it helps you find the few offers worth your time out of hundreds. The system strongly recommends against applying to anything scoring below 4.0/5. Your time is valuable, and so is the recruiter's. Always review before submitting.\n\n> **Heads up: the first evaluations won't be great.** The system doesn't know you yet. Feed it context -- your CV, your career story, your proof points, your preferences, what you're good at, what you want to avoid. The more you nurture it, the better it gets. Think of it as onboarding a new recruiter: the first week they need to learn about you, then they become invaluable.\n\n## Features"
        ),
        (
            "# 5. Personalize with Claude\nclaude   # Open Claude Code in this directory\n\n# Then ask Claude to adapt the system to you:\n# \"Change the archetypes to backend engineering roles\"\n# \"Translate the modes to English\"\n# \"Add these 5 companies to portals.yml\"\n# \"Update my profile with this CV I'm pasting\"\n\n# 6. Start using\n# Paste a job URL or run /career-ops\n```\n\n> **The system is designed to be customized by Claude itself.** Modes, archetypes, scoring weights, negotiation scripts -- just ask Claude to change them. It reads the same files it uses, so it knows exactly what to edit.\n\nSee [docs/SETUP.md](docs/SETUP.md) for the full setup guide.\n"
            ,
            "# 5. Personalize the system\nEdit `config/profile.yml`, `templates/portals.example.yml`, `modes/_shared.md`, and other files directly to match your own career goals. This repository is designed to work without an AI agent, using terminal scripts and manual customization.\n\n# 6. Start using\n# Create your CV and reports, then run the commands below.\n```\n\n> **The system is designed to be customized by you.** Modes, archetypes, scoring weights, negotiation scripts -- edit the source files directly to make the project your own.\n\nSee [docs/SETUP.md](docs/SETUP.md) for the full setup guide.\n"
        ),
        (
            "### With Claude Code (AI Agent)\nCareer-ops is a single slash command with multiple modes:\n\n```\n/career-ops                → Show all available commands\n/career-ops {paste a JD}   → Full auto-pipeline (evaluate + PDF + tracker)\n/career-ops scan           → Scan portals for new offers\n/career-ops pdf            → Generate ATS-optimized CV\n/career-ops batch          → Batch evaluate multiple offers\n/career-ops tracker        → View application status\n/career-ops apply          → Fill application forms with AI\n/career-ops pipeline       → Process pending URLs\n/career-ops contacto       → LinkedIn outreach message\n/career-ops deep           → Deep company research\n/career-ops training       → Evaluate a course/cert\n/career-ops project        → Evaluate a portfolio project\n```\n\nOr just paste a job URL or description directly -- career-ops auto-detects it and runs the full pipeline.\n\n### Without Claude Code (Terminal CLI)\nIf you don't have Claude Code (e.g., using Codex or no AI assistant), use the **terminal-based CLI**:\n\n```powershell\n# Evaluate a job manually\nnode doctor.mjs                    # System health check\nnode verify-pipeline.mjs           # Verify tracker integrity\nnode merge-tracker.mjs             # Merge batch additions\n"
            ,
            "## Manual Workflow\nUse the built-in scripts and markdown files to evaluate offers, generate PDFs, and manage your tracker. External AI helpers are optional, but not required.\n\n```powershell\n# Check system health\nnode doctor.mjs                    # System health check\nnode verify-pipeline.mjs           # Verify tracker integrity\nnode merge-tracker.mjs             # Merge batch additions\nnode normalize-statuses.mjs        # Fix status formatting\nnode generate-pdf.mjs /tmp/cv-custom.html output/cv-company-2026-04-08.pdf --format=a4\n```\n\nFor a full terminal workflow, see [`CLI_GUIDE.md`](CLI_GUIDE.md) or [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md)."
        ),
        (
            "## Tech Stack\n\n![Claude Code](https://img.shields.io/badge/Claude_Code-000?style=flat&logo=anthropic&logoColor=white)\n![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)\n![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white)\n![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)\n![Bubble Tea](https://img.shields.io/badge/Bubble_Tea-FF75B5?style=flat&logo=go&logoColor=white)\n\n- **Agent**: Claude Code with custom skills and modes\n- **PDF**: Playwright/Puppeteer + HTML template\n- **Scanner**: Playwright + Greenhouse API + WebSearch\n- **Dashboard**: Go + Bubble Tea + Lipgloss (Catppuccin Mocha theme)\n- **Data**: Markdown tables + YAML config + TSV batch files\n\n## Also Open Source\n\n- **[cv-santiago](https://github.com/santifer/cv-santiago)** -- The portfolio website (santifer.io) with AI chatbot, LLMOps dashboard, and case studies. If you need a portfolio to showcase alongside your job search, fork it and make it yours.\n\n## About the Author\n\nI'm Santiago -- Head of Applied AI, former founder (built and sold a business that still runs with my name on it). I built career-ops to manage my own job search. It worked: I used it to land my current role.\n\nMy portfolio and other open source projects → [santifer.io](https://santifer.io)\n\n☕ [Buy me a coffee](https://buymeacoffee.com/santifer) if career-ops helped your job search.\n"
            ,
            "## Tech Stack\n\n![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)\n![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white)\n![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)\n![Bubble Tea](https://img.shields.io/badge/Bubble_Tea-FF75B5?style=flat&logo=go&logoColor=white)\n\n- **Automation**: local Node scripts, markdown workflows, and optional AI integration\n- **PDF**: Playwright + HTML template\n- **Scanner**: Playwright + targeted search queries\n- **Dashboard**: Go + Bubble Tea + Lipgloss\n- **Data**: Markdown tables + YAML config + TSV batch files\n"
        ),
    ],
    'README.es.md': [
        (
            "| **Batch** | Evaluacion en paralelo con `claude -p` |\n| **Dashboard TUI** | Terminal UI para navegar, filtrar y ordenar tu pipeline |\n| **Human-in-the-Loop** | La IA evalua y recomienda, tu decides y actuas. El sistema nunca envia una aplicacion -- tu siempre tienes la ultima palabra |\n| **Integridad de pipeline** | Merge automatico, dedup, normalizacion de estados, health checks |\n\n## Inicio rapido\n"
            ,
            "| **Batch** | Evaluacion en paralelo con scripts y flujos de trabajo locales |\n| **Dashboard TUI** | Terminal UI para navegar, filtrar y ordenar tu pipeline |\n| **Human-in-the-Loop** | Las recomendaciones son humanas: tu decides si aplicar o no |\n| **Integridad de pipeline** | Merge automatico, dedup, normalizacion de estados, health checks |\n\n## Inicio rapido\n"
        ),
        (
            "# 5. Personalizar con Claude\nclaude   # Abrir Claude Code en este directorio\n\n# Pidele a Claude que adapte el sistema a ti:\n# \"Cambia los arquetipos a roles de backend\"\n# \"Traduce los modes a ingles\"\n# \"Añade estas empresas a portals.yml\"\n# \"Actualiza mi perfil con este CV que te pego\"\n\n# 6. Usar\n# Pega una URL de oferta o ejecuta /career-ops\n```\n\n> **El sistema esta diseñado para que Claude lo personalice.** Modes, arquetipos, scoring, scripts de negociacion -- solo pidelo. Claude lee los mismos archivos que usa, asi que sabe exactamente que editar.\n"
            ,
            "# 5. Personalizar el sistema\nEdita `config/profile.yml`, `templates/portals.example.yml`, `modes/_shared.md`, y otros archivos directamente para alinear el proyecto con tus propios objetivos. Esta plantilla funciona sin un agente de IA, usando scripts de terminal y personalizacion manual.\n\n# 6. Usar\n# Crea tu CV y reportes, luego ejecuta los comandos siguientes.\n```\n\n> **El sistema esta diseñado para que lo personalices tú.** Modes, arquetipos, scoring, scripts de negociacion -- edita los archivos fuente directamente para adaptar el proyecto a tu flujo de trabajo.\n"
        ),
        (
            "## Uso\n\nCareer-ops es un unico slash command con multiples modos:\n\n```\n/career-ops                → Mostrar todos los comandos\n/career-ops {pega un JD}   → Pipeline completo (evaluar + PDF + tracker)\n/career-ops scan           → Escanear portales\n/career-ops pdf            → Generar CV ATS-optimizado\n/career-ops batch          → Evaluar ofertas en batch\n/career-ops tracker        → Ver estado de aplicaciones\n/career-ops apply          → Rellenar formularios con IA\n/career-ops pipeline       → Procesar URLs pendientes\n/career-ops contacto       → Mensaje LinkedIn outreach\n/career-ops deep           → Research profundo de empresa\n```\n\nO simplemente pega una URL o descripcion de oferta -- career-ops la detecta y ejecuta el pipeline completo.\n"
            ,
            "## Uso manual\n\nUtiliza los scripts incluidos y los archivos markdown para evaluar ofertas, generar PDFs y gestionar tu tracker. La asistencia de IA es opcional y no es obligatoria.\n\n```powershell\n# Revisa el estado del sistema\nnode doctor.mjs\nnode verify-pipeline.mjs\nnode merge-tracker.mjs\nnode normalize-statuses.mjs\nnode generate-pdf.mjs /tmp/cv-custom.html output/cv-company-2026-04-08.pdf --format=a4\n```\n\nPara un flujo completo por terminal, consulta [`CLI_GUIDE.md`](CLI_GUIDE.md) o [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md).\n"
        ),
        (
            "- **Agente**: Claude Code con skills y modos personalizados\n- **PDF**: Playwright/Puppeteer + template HTML\n- **Scanner**: Playwright + Greenhouse API + WebSearch\n- **Dashboard**: Go + Bubble Tea + Lipgloss (tema Catppuccin Mocha)\n- **Datos**: Tablas Markdown + config YAML + ficheros TSV batch\n"
            ,
            "- **Automatizacion**: scripts locales y flujos de trabajo markdown\n- **PDF**: Playwright + template HTML\n- **Scanner**: Playwright + consultas dirigidas\n- **Dashboard**: Go + Bubble Tea + Lipgloss\n- **Datos**: Tablas Markdown + config YAML + ficheros TSV batch\n"
        ),
        (
            "## Tambien Open Source\n\n- **[cv-santiago](https://github.com/santifer/cv-santiago)** -- El portfolio (santifer.io) con chatbot IA, dashboard LLMOps y case studies. Si necesitas un portfolio para acompañar tu busqueda de empleo, echale un vistazo.\n\n## Aviso legal\n"
            ,
            "## Aviso legal\n"
        ),
        (
            "## Sobre el autor\n\nSoy Santiago -- Head of Applied AI, ex-fundador (monte y vendi un negocio que sigue funcionando con mi nombre). Construi career-ops para gestionar mi propia busqueda de empleo. Funciono: lo use para conseguir mi puesto actual.\n\nMi portfolio y otros proyectos open source → [santifer.io](https://santifer.io)\n\n☕ [Invitame a un cafe](https://buymeacoffee.com/santifer) si career-ops te ayudo en tu busqueda.\n\n## Documentacion\n"
            ,
            "## Documentacion\n"
        ),
    ],
    'docs/SETUP.md': [
        (
            "## Prerequisites\n\n- [Claude Code](https://claude.ai/code) installed and configured\n- Node.js 18+ (for PDF generation and utility scripts)\n- (Optional) Go 1.21+ (for the dashboard TUI)\n"
            ,
            "## Prerequisites\n\n- Node.js 18+ (for PDF generation and utility scripts)\n- Playwright installed for PDF generation\n- (Optional) Go 1.21+ (for the dashboard TUI)\n"
        ),
        (
            "## 5. Start using\n\nOpen Claude Code in this directory:\n\n```bash\nclaude\n```\n\nThen paste a job offer URL or description. Career-ops will automatically evaluate it, generate a report, create a tailored PDF, and track it.\n",
            "## 5. Start using\n\nUse the terminal scripts and your markdown files to run the workflow manually:\n\n```bash\nnode doctor.mjs\nnode verify-pipeline.mjs\nnode merge-tracker.mjs\nnode normalize-statuses.mjs\n```\n\nCreate your CV in `cv.md`, add job descriptions to `jds/`, and write evaluation reports in `reports/.\n"
        ),
    ],
    'CLI_GUIDE.md': [
        (
            "# Career-Ops CLI Guide (Without Claude Code)\n\nYou have **Codex** (code completion) but not **Claude Code** (AI agent). This means you can't use interactive AI commands like `/career-ops evaluate [URL]`. However, **you can use everything else through the terminal** by running Node.js scripts and editing files manually.\n"
            ,
            "# Career-Ops CLI Guide\n\nThis guide explains how to use Career-Ops manually without an AI agent. Use Node.js scripts, Playwright, and markdown files to evaluate jobs, generate PDFs, and manage your tracker.\n"
        ),
        (
            "<!-- In templates/cv-template.html, replace: -->\n{{NAME}} → \"Sandro Coelho\"\n{{EMAIL}} → \"sandro@example.com\"\n{{PORTFOLIO_URL}} → \"https://sandrocoelhobr.my.canva.site/\"\n{{PORTFOLIO_DISPLAY}} → \"Portfolio\"\n{{SUMMARY_TEXT}} → \"Diretor cinematográfico com 10+ anos...\"\n{{PORTFOLIO_HIGHLIGHTS}} → HTML of 2-3 key projects with metrics\n{{COMPETENCIES}} → Tags like <span class=\"competency-tag\">Audiovisual</span>\n" 
            ,
            "<!-- In templates/cv-template.html, replace: -->\n{{NAME}} → \"Your Name\"\n{{EMAIL}} → \"you@example.com\"\n{{PORTFOLIO_URL}} → \"https://your-portfolio.example.com\"\n{{PORTFOLIO_DISPLAY}} → \"Portfolio\"\n{{SUMMARY_TEXT}} → \"Creative director and audiovisual producer with 10+ years of experience...\"\n{{PORTFOLIO_HIGHLIGHTS}} → HTML of 2-3 key projects with metrics\n{{COMPETENCIES}} → Tags like <span class=\"competency-tag\">Audiovisual</span>\n"
        ),
        (
            "**Step 2: Save as `/tmp/cv-sandro-company.html`**\n```powershell\nnotepad /tmp/cv-sandro-company.html\n# Paste your customized HTML and save\n```\n"
            ,
            "**Step 2: Save as `/tmp/cv-custom.html`**\n```powershell\nnotepad /tmp/cv-custom.html\n# Paste your customized HTML and save\n```\n"
        ),
        (
            "1. Create `cv-sandro.md` with full resume\n"
            ,
            "1. Create `cv-custom.md` with full resume\n"
        ),
    ],
    'CLI_GUIDE_PT.md': [
        (
            "# Guia CLI Career-Ops (Sem Claude Code)\n\nVocê tem **Codex** (conclusão de código) mas não tem **Claude Code** (agente IA). Isso significa que você não pode usar comandos interativos como `/career-ops avaliar [URL]`. Porém, **você pode usar tudo pelo terminal** executando scripts Node.js e editando arquivos manualmente.\n"
            ,
            "# Guia CLI Career-Ops\n\nEste guia explica como usar o Career-Ops manualmente, sem um agente IA. Use scripts Node.js, Playwright e arquivos markdown para avaliar vagas, gerar PDFs e gerir seu tracker.\n"
        ),
        (
            "{{NAME}} → \"Sandro Coelho\"\n{{EMAIL}} → \"sandro@example.com\"\n{{PORTFOLIO_URL}} → \"https://sandrocoelhobr.my.canva.site/\"\n{{PORTFOLIO_DISPLAY}} → \"Portfólio\"\n{{SUMMARY_TEXT}} → \"Diretor cinematográfico com 10+ anos...\"\n{{PORTFOLIO_HIGHLIGHTS}} → HTML de 2-3 projetos principais com métricas\n{{COMPETENCIES}} → Tags como <span class=\"competency-tag\">Audiovisual</span>\n"
            ,
            "{{NAME}} → \"Seu Nome\"\n{{EMAIL}} → \"voce@example.com\"\n{{PORTFOLIO_URL}} → \"https://seu-portfolio.exemplo.com\"\n{{PORTFOLIO_DISPLAY}} → \"Portfólio\"\n{{SUMMARY_TEXT}} → \"Diretor criativo com 10+ anos de experiência em comunicação audiovisual...\"\n{{PORTFOLIO_HIGHLIGHTS}} → HTML de 2-3 projetos principais com métricas\n{{COMPETENCIES}} → Tags como <span class=\"competency-tag\">Audiovisual</span>\n"
        ),
        (
            "**Passo 2: Salvar como `/tmp/cv-sandro-empresa.html`**\n```powershell\nnotepad /tmp/cv-sandro-empresa.html\n# Cole seu HTML personalizado e salve\n```\n"
            ,
            "**Passo 2: Salvar como `/tmp/cv-custom.html`**\n```powershell\nnotepad /tmp/cv-custom.html\n# Cole seu HTML personalizado e salve\n```\n"
        ),
        (
            "1. Criar `cv-sandro.md` com currículo completo\n"
            ,
            "1. Criar `cv-custom.md` com currículo completo\n"
        ),
    ],
    'QUICK_REFERENCE.md': [
        (
            "- `{{NAME}}` → \"Sandro Coelho\"\n- `{{EMAIL}}` → email@example.com\n- `{{PORTFOLIO_URL}}` → Portfolio link\n"
            ,
            "- `{{NAME}}` → \"Your Name\"\n- `{{EMAIL}}` → email@example.com\n- `{{PORTFOLIO_URL}}` → Portfolio link\n"
        ),
        (
            "node generate-pdf.mjs /tmp/cv-custom.html output/cv-sandro-COMPANY-DATE.pdf --format=a4\n\n# Example:\nnode generate-pdf.mjs /tmp/cv-custom.html output/cv-sandro-ogilvy-2026-04-08.pdf --format=a4\n"
            ,
            "node generate-pdf.mjs /tmp/cv-custom.html output/cv-company-date.pdf --format=a4\n\n# Example:\nnode generate-pdf.mjs /tmp/cv-custom.html output/cv-example-2026-04-08.pdf --format=a4\n"
        ),
    ],
    'QUICK_REFERENCE_PT.md': [
        (
            "- `{{NAME}}` → \"Sandro Coelho\"\n- `{{EMAIL}}` → email@example.com\n- `{{PORTFOLIO_URL}}` → Portfolio link\n"
            ,
            "- `{{NAME}}` → \"Seu Nome\"\n- `{{EMAIL}}` → email@example.com\n- `{{PORTFOLIO_URL}}` → Portfolio link\n"
        ),
        (
            "node generate-pdf.mjs /tmp/cv-custom.html output/cv-sandro-EMPRESA-DATA.pdf --format=a4\n\n# Exemplo:\nnode generate-pdf.mjs /tmp/cv-custom.html output/cv-sandro-ogilvy-2026-04-08.pdf --format=a4\n"
            ,
            "node generate-pdf.mjs /tmp/cv-custom.html output/cv-company-date.pdf --format=a4\n\n# Exemplo:\nnode generate-pdf.mjs /tmp/cv-custom.html output/cv-exemplo-2026-04-08.pdf --format=a4\n"
        ),
    ],
    'GUIA_SIMPLES_PT.md': [
        (
            "**Olá Sandro!** Este guia é para você usar o sistema Career-Ops **sem precisar digitar comandos no computador**. Tudo será feito clicando em arquivos e pastas, como você já sabe fazer no Windows.\n"
            ,
            "**Olá!** Este guia mostra como usar o sistema Career-Ops sem precisar digitar comandos no computador. Tudo pode ser feito com arquivos e pastas no Windows.\n"
        ),
        (
            "candidate:\n  full_name: \"Sandro Coelho\"\n  email: \"sandro.coelho@email.com\"\n  phone: \"+55-11-99999-9999\"\n  location: \"Rio de Janeiro, RJ\"\n  linkedin: \"linkedin.com/in/sandro-coelho\"\n  portfolio_url: \"https://sandrocoelhobr.my.canva.site/\"\n  github: \"github.com/sandrocoelho\"\n"
            ,
            "candidate:\n  full_name: \"Seu Nome\"\n  email: \"voce@example.com\"\n  phone: \"+55-11-99999-9999\"\n  location: \"Sua Cidade, Estado\"\n  linkedin: \"linkedin.com/in/seu-perfil\"\n  portfolio_url: \"https://seu-portfolio.exemplo.com\"\n  github: \"github.com/seu-usuario\"\n"
        ),
        (
            "# Sandro Coelho\n"
            ,
            "# Seu Nome\n"
        ),
        (
            "{{NAME}} → Sandro Coelho\n{{EMAIL}} → sandro.coelho@email.com\n{{PORTFOLIO_URL}} → https://sandrocoelhobr.my.canva.site/\n"
            ,
            "{{NAME}} → Seu Nome\n{{EMAIL}} → voce@example.com\n{{PORTFOLIO_URL}} → https://seu-portfolio.exemplo.com\n"
        ),
        (
            "2. Salve na pasta `output/` como `cv-sandro-empresa.html`\nnode generate-pdf.mjs output/cv-sandro-empresa.html output/cv-sandro-empresa-2026-04-08.pdf --format=a4\n"
            ,
            "2. Salve na pasta `output/` como `cv-custom.html`\nnode generate-pdf.mjs output/cv-custom.html output/cv-example-2026-04-08.pdf --format=a4\n"
        ),
    ],
    'config/profile.example.yml': [
        (None, "# Career-Ops Profile Configuration\n# Copy this file to config/profile.yml and fill in your details.\n# This is the single source of truth for your personal data across all modes.\n\ncandidate:\n  full_name: \"Your Name\"\n  email: \"you@example.com\"\n  phone: \"+55-11-99999-9999\"\n  location: \"Your City, State\"\n  linkedin: \"linkedin.com/in/your-profile\"\n  portfolio_url: \"https://your-portfolio.example.com\"\n  github: \"github.com/your-username\"\n  twitter: \"https://x.com/your-handle\"\n\ntarget_roles:\n  primary:\n    - \"Creative Director\"\n    - \"Audiovisual Producer\"\n    - \"Visual Storyteller\"\n  archetypes:\n    - name: \"Creative Director\"\n      level: \"Senior\"\n      fit: \"primary\"\n    - name: \"Audiovisual Producer\"\n      level: \"Senior\"\n      fit: \"primary\"\n    - name: \"Motion Designer\"\n      level: \"Mid-Senior\"\n      fit: \"secondary\"\n    - name: \"Content Director\"\n      level: \"Senior\"\n      fit: \"adjacent\"\n\nnarrative:\n  headline: \"Creative director and audiovisual storyteller with experience in branded content and campaigns\"\n  exit_story: \"I create high-impact audiovisual content that connects brands and audiences through narrative-driven production.\"\n  superpowers:\n    - \"Creative direction and visual storytelling\"\n    - \"Audiovisual production and team coordination\"\n    - \"Motion design and post-production\"\n    - \"Brand communication and campaign execution\"\n  proof_points:\n    - name: \"Branded Campaign\"\n      url: \"https://your-portfolio.example.com/project-a\"\n      hero_metric: \"Increased brand awareness by 40%\"\n    - name: \"Institutional Video\"\n      url: \"https://your-portfolio.example.com/project-b\"\n      hero_metric: \"2M+ views and high employee engagement\"\n    - name: \"Creative Campaign\"\n      url: \"https://your-portfolio.example.com/project-c\"\n      hero_metric: \"Improved internal communication adoption by 30%\"\n\ncompensation:\n  target_range: \"R$ 8.000-12.000\"\n  currency: \"BRL\"\n  minimum: \"R$ 6.000\"\n  location_flexibility: \"Remote preferred, open to hybrid arrangements\"\n\nlocation:\n  country: \"Brazil\"\n  city: \"Your City\"\n  timezone: \"BRT\"\n  visa_status: \"Brazilian citizen\"\n"
        ),
    ],
    'config/profile.yml': [
        (None, "# Career-Ops Profile Configuration\n# Copy this file to config/profile.yml and fill in your details.\n# This is the single source of truth for your personal data across all modes.\n\ncandidate:\n  full_name: \"Your Name\"\n  email: \"you@example.com\"\n  phone: \"+55-11-99999-9999\"\n  location: \"Your City, State\"\n  linkedin: \"linkedin.com/in/your-profile\"\n  portfolio_url: \"https://your-portfolio.example.com\"\n  github: \"github.com/your-username\"\n  twitter: \"https://x.com/your-handle\"\n\ntarget_roles:\n  primary:\n    - \"Creative Director\"\n    - \"Audiovisual Producer\"\n    - \"Visual Storyteller\"\n  archetypes:\n    - name: \"Creative Director\"\n      level: \"Senior\"\n      fit: \"primary\"\n    - name: \"Audiovisual Producer\"\n      level: \"Senior\"\n      fit: \"primary\"\n    - name: \"Motion Designer\"\n      level: \"Mid-Senior\"\n      fit: \"secondary\"\n    - name: \"Content Director\"\n      level: \"Senior\"\n      fit: \"adjacent\"\n\nnarrative:\n  headline: \"Creative director and audiovisual storyteller with experience in branded content and campaigns\"\n  exit_story: \"I create high-impact audiovisual content that connects brands and audiences through narrative-driven production.\"\n  superpowers:\n    - \"Creative direction and visual storytelling\"\n    - \"Audiovisual production and team coordination\"\n    - \"Motion design and post-production\"\n    - \"Brand communication and campaign execution\"\n  proof_points:\n    - name: \"Branded Campaign\"\n      url: \"https://your-portfolio.example.com/project-a\"\n      hero_metric: \"Increased brand awareness by 40%\"\n    - name: \"Institutional Video\"\n      url: \"https://your-portfolio.example.com/project-b\"\n      hero_metric: \"2M+ views and high engagement\"\n    - name: \"Creative Campaign\"\n      url: \"https://your-portfolio.example.com/project-c\"\n      hero_metric: \"Improved internal communication adoption by 30%\"\n\ncompensation:\n  target_range: \"R$ 8.000-12.000\"\n  currency: \"BRL\"\n  minimum: \"R$ 6.000\"\n  location_flexibility: \"Remote preferred, open to hybrid arrangements\"\n\nlocation:\n  country: \"Brazil\"\n  city: \"Your City\"\n  timezone: \"BRT\"\n  visa_status: \"Brazilian citizen\"\n"
        ),
    ],
    'CONTRIBUTING.md': [
        ("Thanks for your interest in contributing! Career-Ops is built with Claude Code, and you can use it for development too.\n", "Thanks for your interest in contributing! Career-Ops is a customizable career toolkit that can be used with terminal scripts, local workflows, and optional AI assistance.\n")
    ],
    'CREATIVE_ADAPTATION_PLAN.md': [
        ("Adapt the career-ops repository to support non-tech creative job searches for clients based in Brazil. The system will maintain its core structure while shifting focus from AI/tech roles to creative professions, specifically tailored for audiovisual professionals like Sandro Coelho with expertise in film direction, audiovisual production, videomaking, photography, motion design, and internal communications.\n",
         "Adapt the career-ops repository to support non-tech creative job searches for clients in Brazil. The system will maintain its core structure while shifting focus from creative professions, specifically tailored for audiovisual and branded-content roles with expertise in film direction, audiovisual production, videomaking, photography, motion design, and internal communications.\n")
    ],
    'docs/CUSTOMIZATION.md': [
        ("Career-ops can integrate with external systems via Claude Code hooks. Example hooks:\n",
         "Career-ops can integrate with external systems via optional hooks. Example hooks:\n")
    ],
    'package.json': [
        ("  \"keywords\": [\"ai\", \"job-search\", \"claude-code\", \"career\", \"automation\"],\n  \"author\": \"Santiago Fernández de Valderrama <hi@santifer.io> (https://santifer.io)\",\n",
         "  \"keywords\": [\"job-search\", \"career\", \"automation\"],\n  \"author\": \"Wancoe\",\n")
    ],
    'CITATION.cff': [
        ("  - claude-code\n",
         "  - career-opstemplate\n")
    ],
}

for path, ops in replacements.items():
    p = Path(path)
    if not p.exists():
        print(f'MISSING: {path}')
        continue
    text = p.read_text(encoding='utf-8')
    for old, new in ops:
        if old is None:
            text = new
        else:
            if old not in text:
                print(f'MISSING BLOCK in {path}: {repr(old[:80])}...')
            text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print(f'updated {path}')

# Clean up personal sample artifacts and rename personal sample files
output_file = Path('output/cv-sandro-empresa-2026-04-08.html')
if output_file.exists():
    output_file.unlink()
    print('removed output artifact')

for old_name, new_name in [
    ('templates/cv-sandro-empresa.md', 'templates/cv-sample.md'),
    ('examples/cv-sandro-example.md', 'examples/cv-sample.md'),
]:
    old_path = Path(old_name)
    new_path = Path(new_name)
    if old_path.exists():
        if new_path.exists():
            new_path.unlink()
        old_path.rename(new_path)
        print(f'renamed {old_name} -> {new_name}')
