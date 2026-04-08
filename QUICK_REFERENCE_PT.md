# Referência Rápida — Comandos CLI do Career-Ops (PT-BR)

## Configuração (Uma única vez)

```powershell
# 1. Instale Node.js em https://nodejs.org/

# 2. Verifique instalação
node --version
npm --version

# 3. Instale Playwright (necessário para PDF)
npx playwright install chromium

# 4. Copie arquivos de exemplo
Copy-Item config/profile.example.yml config/profile.yml
Copy-Item templates/portals.example.yml portals.yml

# 5. Crie diretórios necessários
New-Item -ItemType Directory output,reports,jds,batch/tracker-additions -Force

# 6. Crie arquivos de CV e digest
New-Item cv.md -Type File
New-Item article-digest.md -Type File
```

---

## Fluxo de Trabalho Diário

### 1. Verificar Saúde do Sistema
```powershell
node doctor.mjs
```
Corrige qualquer arquivo ausente ou problemas de config.

### 2. Avaliar uma Vaga (Passos Manuais)

**A. Salvar a descripção da vaga**
```powershell
# Cole texto de vaga em arquivo
@'
[Descrição completa da vaga aqui]
'@ | Set-Content jds/vaga-01.txt
```

**B. Ler rubrica de avaliação**
```powershell
Get-Content modes/pt/oferta.md  # Avaliação em português
```

**C. Criar relatório de avaliação**
- Criar arquivo: `reports/001-empresa-nome-YYYY-MM-DD.md`
- Copiar template de `examples/sample-report.md`
- Preencher Blocos A-F com suas pontuações manuais
- Adicionar recomendação: "Candidatar-se" / "Não candidatar" / "Considerar se..."

**D. Adicionar ao rastreador**
```powershell
# Edite data/applications.md e adicione uma linha:
# | 1 | 2026-04-08 | Empresa | Posição | 4.2/5 | Avaliada | ❌ | [001](reports/001-...) | Notas |
notepad data/applications.md
```

### 3. Gerar Currículo Personalizado em PDF

**A. Editar template HTML**
```powershell
# Copiar para /tmp/
Copy-Item templates/cv-template.html /tmp/cv-custom.html

# Abrir e editar placeholders
notepad /tmp/cv-custom.html
```

Substitua:
- `{{NAME}}` → "Seu Nome"
- `{{EMAIL}}` → email@example.com
- `{{PORTFOLIO_URL}}` → Link de portfólio
- `{{SUMMARY_TEXT}}` → 3-4 linhas compatíveis com vaga
- `{{PORTFOLIO_HIGHLIGHTS}}` → 2-3 projetos-chave (com métricas e links)
- `{{COMPETENCIES}}` → 6-8 tags de skill compatíveis com vaga
- `{{EXPERIENCE}}` → Reordene bullets por relevância à vaga

**B. Gerar PDF**
```powershell
# Formato: a4 para Brasil/global, letter para US/Canadá
node generate-pdf.mjs /tmp/cv-custom.html output/cv-company-date.pdf --format=a4

# Exemplo:
node generate-pdf.mjs /tmp/cv-custom.html output/cv-exemplo-2026-04-08.pdf --format=a4
```

**C. Verificar PDF criado**
```powershell
Get-Item output/cv-*.pdf | Select-Object Name, Length
```

### 4. Rastrear Candidaturas

```powershell
# Ver candidaturas atuais
Get-Content data/applications.md

# Editar para atualizar status
notepad data/applications.md
# Mude status: Avaliada → Candidatura Enviada → Entrevista → Oferta, etc.

# Mesclar adições se usar modo batch
node merge-tracker.mjs

# Verificar integridade
node verify-pipeline.mjs

# Corrigir entradas duplicadas
node dedup-tracker.mjs

# Corrigir formatação de status
node normalize-statuses.mjs
```

---

## Arquivos e Caminhos Importantes

| Arquivo | Propósito |
|---------|-----------|
| `config/profile.yml` | Seus dados pessoais (nome, email, portfólio) |
| `cv.md` | Seu currículo completo (única fonte de verdade) |
| `article-digest.md` | Projetos de portfólio com métricas |
| `data/applications.md` | Rastreador de todas as candidaturas |
| `data/pipeline.md` | URLs aguardando avaliação |
| `portals.yml` | Configuração de busca em portais |
| `templates/cv-template.html` | Template de currículo para geração de PDF |
| `modes/pt/oferta.md` | Rubrica de avaliação (Blocos A-F) em português |
| `reports/` | Armazene relatórios de avaliação aqui |
| `output/` | PDFs vão aqui |

---

## Dicas para Personalizar Currículo Criativo

### Personalizar para Papéis de Marca/Campanha

**Em `{{SUMMARY_TEXT}}`:**
```
Diretor cinematográfico com 10+ anos criando conteúdo impactante.
Experiência em direção de campanhas de marca (ROI +40%), produção 
audiovisual em larga escala e comunicação corporativa.
```

**Em `{{PORTFOLIO_HIGHLIGHTS}}`:**
```html
<li class="portfolio-item">
  <strong>Campanha "Marca X" (2024)</strong> — Direção, 2M+ visualizações, 
  95% engajamento. <a href="https://portfolio.com/campaign">Link</a>
</li>
<li class="portfolio-item">
  <strong>Vídeo Institucional Y (2023)</strong> — Produção e direção, 
  redução de rotatividade 60%. <a href="https://portfolio.com/video">Link</a>
</li>
```

**Em `{{COMPETENCIES}}`:**
```html
<span class="competency-tag">Direção Cinematográfica</span>
<span class="competency-tag">Produção Audiovisual</span>
<span class="competency-tag">Motion Design</span>
<span class="competency-tag">Estratégia de Marca</span>
<span class="competency-tag">Storytelling</span>
<span class="competency-tag">Comunicação Corporativa</span>
```

---

## Operações em Lote

### Processar múltiplas vagas de uma vez
```powershell
# Criar arquivos TSV em batch/tracker-additions/
# Formato: num, data, empresa, posição, status, pontuação, pdf, relatório, notas

# Exemplo: batch/tracker-additions/001-empresa.tsv
# 1	2026-04-08	Empresa A	Diretor	Avaliada	4.2/5	❌	[001](reports/001-empresa-a-2026-04-08.md)	Bom encaixe

# Mesclar tudo no rastreador
node merge-tracker.mjs
```

---

## Valores de Status (Use Exatamente)

Ao atualizar `data/applications.md`, use apenas estes statuses:
- `Avaliada` — Relatório concluído, pronto para decidir
- `Candidatura Enviada` — Candidatura enviada
- `Respondida` — Empresa respondeu
- `Entrevista` — Entrevista agendada ou em progresso
- `Oferta` — Oferta recebida
- `Rejeitada` — Empresa rejeitou
- `Descartada` — Você rejeitou ou oportunidade fechou
- `SKIP` — Não encaixa, não vai candidatar

---

## Solução de Problemas

**Problema: Node.js não encontrado**
```powershell
# Reinstale a partir de https://nodejs.org/
# Reinicie PowerShell após instalar
node --version
```

**Problema: Geração de PDF falha**
```powershell
# Verificar dependências
node doctor.mjs

# Instalar Playwright se ausente
npx playwright install chromium
```

**Problema: Rastreador não mescla**
```powershell
# Verificar formato TSV em batch/tracker-additions/
node verify-pipeline.mjs  # Mostra erros

# Remover duplicatas se existirem
node dedup-tracker.mjs
```

---

## Dicas Codex (Conclusão de Código)

Peça ao Codex para ajudar com:
1. **Formatação HTML** — "Corrigir seção de Destaques de Portfólio em cv-template.html"
2. **Conteúdo PT-BR** — "Escrever resumo profissional em português para um diretor criativo"
3. **Templates Markdown** — "Criar template de relatório de avaliação para vaga de diretor de marca"
4. **Scripts** — "Escrever script PowerShell para renomear PDFs em lote por nome da empresa"

---

## Para Português (Modo Português)

Use arquivos `modes/pt/` em vez de inglês, especialmente para:
- `modes/pt/_shared.md` — Arquetipos e regras de pontuação em português
- `modes/pt/oferta.md` — Rubrica de avaliação (Blocos A-F) em português
- `modes/pt/pdf.md` — Orientação de geração de PDF em português

Quando quiser output em português, consulte `modes/pt/oferta.md` para regras de avaliação em vez da versão em inglês.

---

## Próximo: Testar Geração de PDF

1. **Editar `templates/cv-template.html`** com dados de amostra
2. **Salvar em `/tmp/test.html`**
3. **Executar:** `node generate-pdf.mjs /tmp/test.html output/test.pdf --format=a4`
4. **Verificar:** `output/test.pdf` deve existir

Pronto! Você agora tem um sistema de busca de carreira funcionando baseado em terminal.
