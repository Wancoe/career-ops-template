# Career-Ops CLI Guide

This guide explains how to use Career-Ops manually without an AI agent. Use Node.js scripts, Playwright, and markdown files to evaluate jobs, generate PDFs, and manage your tracker.

---

## Quick Start (5 minutes)

### Prerequisites
1. **Node.js 18+** → Download from [nodejs.org](https://nodejs.org/)
2. **Playwright** → After Node.js install, run:
   ```powershell
   npx playwright install chromium
   ```
3. **Git** (optional, for version control)

Verify:
```powershell
node --version
npm --version
```

### First Run - Setup
```powershell
# Copy example configs
Copy-Item config/profile.example.yml config/profile.yml
Copy-Item templates/portals.example.yml portals.yml

# Create data files
New-Item data/applications.md -Type File -Force
New-Item data/pipeline.md -Type File -Force
New-Item cv.md -Type File -Force
New-Item article-digest.md -Type File -Force

# Create directories
New-Item -ItemType Directory output,reports,jds,batch/tracker-additions -Force
```

---

## Feature 1: Job Evaluation (Manual)

### What You Do
You read a job description, manually score it using the career-ops rubric, and generate a report.

### How

**Step 1: Read the rubric**
```powershell
# Windows: open the evaluation rules
Get-Content modes/oferta.md
# Look for "Bloques A-F" (Blocks A-F)
```

**Step 2: Copy a job description to `jds/job.txt`**
```powershell
@'
[Paste the full job description here]
'@ | Set-Content jds/job.txt
```

**Step 3: Score manually using the blocks**
Open `modes/oferta.md` and score:
- **Block A**: Skill match (1-5)
- **Block B**: Role fit (1-5)
- **Block C**: Compensation (1-5)
- **Block D**: Culture (1-5)
- **Block E**: Red flags (negative adjustments)
- **Block F**: Overall score

**Step 4: Generate evaluation report**
Create `reports/001-company-name-2026-04-08.md`:
```markdown
# Evaluation Report

**URL:** https://example.com/job

**Company:** Exemplo
**Role:** Diretor Criativo
**Date:** 2026-04-08

## Score: 4.2/5

### Block A: CV Match
- [Your skills match assessment]

### Block B: North Star Alignment
- [Does it fit target roles?]

### Block C: Compensation
- Offered: R$ 8,000
- Target: R$ 8,000-12,000
- Rating: 4/5

### Block D: Cultural Signals
- [Company culture assessment]

### Block E: Red Flags
- [Warning signs?]

### Block F: Global Assessment
- Overall: 4.2/5
- Recommendation: Apply
```

**Step 5: Add to tracker**
Edit `data/applications.md`:
```markdown
| # | Date | Company | Role | Score | Status | PDF | Report | Notes |
|---|------|---------|------|-------|--------|-----|--------|-------|
| 1 | 2026-04-08 | Exemplo | Diretor Criativo | 4.2/5 | Evaluated | ❌ | [001](reports/001-exemplo-2026-04-08.md) | Good fit, matches brand work |
```

---

## Feature 2: PDF Generation (Automated)

### What You Do
Create a tailored CV via HTML, then convert to PDF using the script.

### How

**Step 1: Create HTML file**
Use `templates/cv-template.html` as base. Replace placeholders:
```html
<!-- In templates/cv-template.html, replace: -->
{{NAME}} → "Your Name"
{{EMAIL}} → "you@example.com"
{{PORTFOLIO_URL}} → "https://your-portfolio.example.com"
{{PORTFOLIO_DISPLAY}} → "Portfolio"
{{SUMMARY_TEXT}} → "Creative director and audiovisual producer with 10+ years of experience..."
{{PORTFOLIO_HIGHLIGHTS}} → HTML of 2-3 key projects with metrics
{{COMPETENCIES}} → Tags like <span class="competency-tag">Audiovisual</span>
```

**Step 2: Save as `/tmp/cv-custom.html`**
```powershell
notepad /tmp/cv-custom.html
# Paste your customized HTML and save
```

**Step 3: Generate PDF**
```powershell
node generate-pdf.mjs /tmp/cv-custom.html output/cv-example-2026-04-08.pdf --format=a4
```

**Step 4: Verify**
Check the PDF was created:
```powershell
Get-Item output/cv-*.pdf
```

### Example: Tailoring for Brand/Campaign Role
Edit the summary to highlight campaign achievements:

```html
{{SUMMARY_TEXT}} → 
"Diretor cinematográfico especializado em campanhas de marca. 
Liderou produção de conteúdo que alcançou 2M+ visualizações e 
40% aumento em reconhecimento de marca. Experiência em 
direção, produção audiovisual e comunicação interna corporativa."
```

---

## Feature 3: Portal Scanning (Manual)

### What You Do
Check job boards and track new opportunities.

### How

**Step 1: Edit `portals.yml` search queries**
The file already has creative role filters for:
- LinkedIn Brasil
- Vagas.com.br
- Catho
- Indeed Brasil
- Behance
- Dribbble

**Step 2: Check manually or add to pipeline**
Edit `data/pipeline.md` with new URLs:
```markdown
# Pipeline - Pending URLs

- https://www.linkedin.com/jobs/view/123456789
- https://job-board.com/creative-director-rio
- https://vagas.com.br/vaga/12345
```

**Step 3: Move to applications with evaluation**
Once evaluated, move URL from pipeline.md to applications.md with status.

---

## Feature 4: Batch Tracker Management (Scripts)

### Merge tracker additions
If you create TSV files in `batch/tracker-additions/`:
```powershell
node merge-tracker.mjs
```

### Verify tracker integrity
```powershell
node verify-pipeline.mjs
```

### Normalize statuses
```powershell
node normalize-statuses.mjs
```

### Dedup duplicates
```powershell
node dedup-tracker.mjs
```

---

## Feature 5: System Health Check

### Diagnostic helper
```powershell
node doctor.mjs
```

This checks:
- Required files exist
- Fonts are in place
- Config files are valid
- Node.js and Playwright setup

### Check for updates
```powershell
node update-system.mjs check
```

---

## Feature 6: Creative Resume Tailoring (With Your Setup)

### Custom profile
Edit `config/profile.yml`:
```yaml
candidate:
  full_name: "Your Name"
  email: "you@example.com"
  portfolio_url: "https://your-portfolio.example.com/"
  
target_roles:
  primary:
    - "Diretor Cinematográfico"
    - "Produtor Audiovisual"

narrative:
  headline: "Diretor cinematográfico com 10+ anos"
  exit_story: "Especialista em audiovisual..."
  proof_points:
    - name: "Campanha Marca X"
      url: "https://portfolio.com/project1"
      hero_metric: "2M+ visualizações"
```

### Example CV workflow
1. Create `cv-custom.md` with full resume
2. Create `article-digest.md` with portfolio projects
3. For each job, copy `templates/cv-template.html`
4. Edit placeholders with job-specific keywords
5. Run `node generate-pdf.mjs` to generate PDF
6. Track in `data/applications.md`

---

## Complete Workflow Example

### Scenario: Apply to a Creative Director role in Rio

**1. Find the job**
- Save URL to `data/pipeline.md`
- Read full JD

**2. Evaluate**
- Open `modes/oferta.md`
- Read the blocks (A-F scoring)
- Score: 4.3/5 → Recommendation: Apply

**3. Create evaluation report**
- Create `reports/001-company-rio-2026-04-08.md`
- Run: `Get-Content modes/oferta.md > reports/001-company-rio-2026-04-08.md`
- Add your manual scores

**4. Tailor CV**
- Open `templates/cv-template.html` in editor
- Replace `{{...}}` placeholders:
  - Name, email, portfolio
  - Summary: "Diretor com expertise em campanhas..."
  - Portfolio Highlights: 2-3 Rio/brand work projects
  - Competencies: Creative Director, Audiovisual, Brand Strategy
  - Experience: Reorder bullets by relevance
- Save to `/tmp/cv-custom.html`

**5. Generate PDF**
```powershell
node generate-pdf.mjs /tmp/cv-sandro-creativo-rio.html output/cv-sandro-creativo-rio-2026-04-08.pdf --format=a4
```

**6. Track**
Edit `data/applications.md`:
```markdown
| 1 | 2026-04-08 | Company Rio | Diretor Criativo | 4.3/5 | Applied | ✅ | [001](reports/001-company-rio-2026-04-08.md) | Great fit, applied 04-08 |
```

**7. Manage**
- Keep reports organized in `reports/`
- Update status when company responds
- Move to "Interview", "Offer", "Rejected", etc.

---

## Codex Integration Tips

You have **Codex** (ChatGPT code completion). Use it to:

1. **Write HTML customizations**
   - Codex will help you format the CV template
   - Ask Codex to generate PT-BR section labels
   - Generate creative bullet points for experience

2. **Edit modes/ for custom logic**
   - Modify `modes/_shared.md` archetype scoring
   - Update `modes/pt/_profile.md` with custom narrative

3. **Create helper scripts**
   - Ask Codex to write a PowerShell script that automates steps
   - Generate batch processors for evaluations

4. **Write cover letters**
   - Use Codex to draft PT-BR or EN cover letters
   - Tailor using keywords from job descriptions

---

## Summary

| Feature | How to Use |
|---------|-----------|
| **Job Evaluation** | Manual scoring using `modes/oferta.md` rubric |
| **PDF Generation** | Edit HTML template + run `node generate-pdf.mjs` |
| **Portal Scanning** | Update `portals.yml` + check manually or WebSearch |
| **Tracker Management** | Edit `data/applications.md` + run merge/verify scripts |
| **System Health** | Run `node doctor.mjs` and `node update-system.mjs check` |
| **Custom Resumes** | Edit HTML, inject keywords, generate with Node.js |
| **Code Help** | Use Codex for writing/editing |

---

## Next Steps

1. **Install Node.js** now if you haven't
2. **Run `node doctor.mjs`** to check setup
3. **Test PDF generation** with a simple HTML file
4. **Create your first evaluation** manually
5. **Generate a tailored CV** for a test job

You can do **everything** manually through the terminal instead of using chat commands. It's more work but fully functional!

Questions? Check `README.md` or `docs/SETUP.md` for more details.
