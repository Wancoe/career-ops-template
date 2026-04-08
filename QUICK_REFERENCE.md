# Quick Reference — Career-Ops Terminal Commands

## Setup (One-time)

```powershell
# 1. Install Node.js from https://nodejs.org/

# 2. Verify installation
node --version
npm --version

# 3. Install Playwright (required for PDF)
npx playwright install chromium

# 4. Copy example files
Copy-Item config/profile.example.yml config/profile.yml
Copy-Item templates/portals.example.yml portals.yml

# 5. Create needed directories
New-Item -ItemType Directory output,reports,jds,batch/tracker-additions -Force

# 6. Create CV and digest files
New-Item cv.md -Type File
New-Item article-digest.md -Type File
```

---

## Daily Workflow

### 1. Check System Health
```powershell
node doctor.mjs
```
Fixes any missing files or config issues.

### 2. Evaluate a Job (Manual Steps)

**A. Save the job description**
```powershell
# Paste job text into a file
@'
[Full job description here]
'@ | Set-Content jds/job-01.txt
```

**B. Read evaluation rubric**
```powershell
Get-Content modes/oferta.md  # or modes/pt/oferta.md for Portuguese
```

**C. Create evaluation report**
- Create file: `reports/001-company-name-DATE.md`
- Copy the template from `examples/sample-report.md`
- Fill in Blocks A-F with your manual scores
- Add recommendation: "Apply" / "Don't apply" / "Consider if..."

**D. Add to tracker**
```powershell
# Edit data/applications.md and add a row:
# | 1 | 2026-04-08 | Company | Role | 4.2/5 | Evaluated | ❌ | [001](reports/001-...) | Notes |
notepad data/applications.md
```

### 3. Generate Tailored Resume PDF

**A. Edit HTML template**
```powershell
# Copy to /tmp/
Copy-Item templates/cv-template.html /tmp/cv-custom.html

# Open and edit placeholders
notepad /tmp/cv-custom.html
```

Replace these:
- `{{NAME}}` → "Sandro Coelho"
- `{{EMAIL}}` → email@example.com
- `{{PORTFOLIO_URL}}` → Portfolio link
- `{{SUMMARY_TEXT}}` → 3-4 lines matching the job
- `{{PORTFOLIO_HIGHLIGHTS}}` → 2-3 key projects (with metrics & links)
- `{{COMPETENCIES}}` → 6-8 skill tags matched to job
- `{{EXPERIENCE}}` → Reorder bullets by relevance to job

**B. Generate PDF**
```powershell
# Format: a4 for Brazil/global, letter for US/Canada
node generate-pdf.mjs /tmp/cv-custom.html output/cv-sandro-COMPANY-DATE.pdf --format=a4

# Example:
node generate-pdf.mjs /tmp/cv-custom.html output/cv-sandro-ogilvy-2026-04-08.pdf --format=a4
```

**C. Verify PDF created**
```powershell
Get-Item output/cv-*.pdf | Select-Object Name, Length
```

### 4. Track Applications

```powershell
# View current applications
Get-Content data/applications.md

# Edit to update status
notepad data/applications.md
# Change status: Evaluated → Applied → Interview → Offer, etc.

# Merge additions if using batch mode
node merge-tracker.mjs

# Verify integrity
node verify-pipeline.mjs

# Fix duplicate entries
node dedup-tracker.mjs

# Fix status formatting
node normalize-statuses.mjs
```

---

## Important Files & Paths

| File | Purpose |
|------|---------|
| `config/profile.yml` | Your personal data (name, email, portfolio) |
| `cv.md` | Your full resume (single source of truth) |
| `article-digest.md` | Portfolio projects with metrics |
| `data/applications.md` | Tracker of all applications |
| `data/pipeline.md` | URLs waiting to be evaluated |
| `portals.yml` | Job board search config |
| `templates/cv-template.html` | Resume template for PDF generation |
| `modes/oferta.md` or `modes/pt/oferta.md` | Evaluation rubric (A-F blocks) |
| `reports/` | Store evaluation reports here |
| `output/` | PDFs go here |

---

## Creative Resume Tips

### Tailor for Brand/Campaign Roles

**In `{{SUMMARY_TEXT}}`:**
```
Diretor cinematográfico com 10+ anos criando conteúdo impactante.
Experiência em direção de campanhas de marca (ROI +40%), produção 
audiovisual em alta escala e comunicação corporativa.
```

**In `{{PORTFOLIO_HIGHLIGHTS}}`:**
```html
<li class="portfolio-item">
  <strong>Campanha "Brand X" (2024)</strong> — Direção, 2M+ views, 
  95% engagement. <a href="https://portfolio.com/campaign">Link</a>
</li>
<li class="portfolio-item">
  <strong>Vídeo Institucional Y (2023)</strong> — Produção e direção, 
  redução de turnover 60%. <a href="https://portfolio.com/video">Link</a>
</li>
```

**In `{{COMPETENCIES}}`:**
```html
<span class="competency-tag">Direção Cinematográfica</span>
<span class="competency-tag">Produção Audiovisual</span>
<span class="competency-tag">Motion Design</span>
<span class="competency-tag">Brand Strategy</span>
<span class="competency-tag">Storytelling</span>
<span class="competency-tag">Comunicação Corporativa</span>
```

---

## Batch Operations

### Process multiple jobs at once
```powershell
# Create TSV files in batch/tracker-additions/
# Format: num, date, company, role, status, score, pdf, report, notes

# Example: batch/tracker-additions/001-company.tsv
# 1	2026-04-08	Company A	Diretor	Evaluated	4.2/5	❌	[001](reports/001-company-a-2026-04-08.md)	Good fit

# Merge all into tracker
node merge-tracker.mjs
```

---

## Status Values (Use Exactly)

When updating `data/applications.md`, use only these statuses:
- `Evaluated` — Report completed, ready to decide
- `Applied` — Application sent
- `Responded` — Company replied
- `Interview` — Interview scheduled or in progress
- `Offer` — Offer received
- `Rejected` — Company rejected
- `Discarded` — You rejected or opportunity closed
- `SKIP` — Doesn't fit, won't apply

---

## Troubleshooting

**Problem: Node.js not found**
```powershell
# Re-install from https://nodejs.org/
# Restart PowerShell after install
node --version
```

**Problem: PDF generation fails**
```powershell
# Check dependencies
node doctor.mjs

# Install Playwright if missing
npx playwright install chromium
```

**Problem: Tracker won't merge**
```powershell
# Check TSV format in batch/tracker-additions/
node verify-pipeline.mjs  # Shows errors

# Dedup if duplicates exist
node dedup-tracker.mjs
```

---

## Codex Tips (Code Completion)

Ask Codex to help with:
1. **HTML formatting** — "Fix the Portal Highlights section in cv-template.html"
2. **PT-BR content** — "Write a professional summary in Portuguese for a creative director"
3. **Markdown templates** — "Create an evaluation report template for a brand director role"
4. **Scripts** — "Write a PowerShell script to batch-rename PDFs by company name"

---

## For Portuguese (Modo Português)

Use `modes/pt/` files instead of English, especially for:
- `modes/pt/_shared.md` — Archetypes and scoring rules in Portuguese
- `modes/pt/oferta.md` — Evaluation rubric (Blocos A-F) in Portuguese
- `modes/pt/pdf.md` — PDF generation guidance in Portuguese

When you want Portuguese output, reference `modes/pt/oferta.md` for evaluation rules instead of the English version.

---

## Next: Test PDF Generation

1. **Edit `templates/cv-template.html`** with sample data
2. **Save to `/tmp/test.html`**
3. **Run:** `node generate-pdf.mjs /tmp/test.html output/test.pdf --format=a4`
4. **Check:** `output/test.pdf` should exist

Done! You now have a working terminal-based career search system.
