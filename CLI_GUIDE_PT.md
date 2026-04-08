# Guia CLI Career-Ops

Este projeto está publicado em: https://github.com/Wancoe/career-ops-template

Este guia explica como usar o Career-Ops manualmente, sem um agente IA. Use scripts Node.js, Playwright e arquivos markdown para avaliar vagas, gerar PDFs e gerir seu tracker.

---

## Início Rápido (5 minutos)

### Pré-requisitos
1. **Node.js 18+** → Download em [nodejs.org](https://nodejs.org/)
2. **Playwright** → Após instalar Node.js, execute:
   ```powershell
   npx playwright install chromium
   ```
3. **Git** (opcional, para controle de versão)

Verifique:
```powershell
node --version
npm --version
```

### Primeira Execução - Configuração
```powershell
# Copiar arquivos de exemplo
Copy-Item config/profile.example.yml config/profile.yml
Copy-Item templates/portals.example.yml portals.yml

# Criar arquivos de dados
New-Item data/applications.md -Type File -Force
New-Item data/pipeline.md -Type File -Force
New-Item cv.md -Type File -Force
New-Item article-digest.md -Type File -Force

# Criar diretórios
New-Item -ItemType Directory output,reports,jds,batch/tracker-additions -Force
```

---

## Funcionalidade 1: Avaliação de Vagas (Manual)

### O Que Fazer
Você lê uma descrição de vaga, avalia manualmente usando a rubrica do career-ops e gera um relatório.

### Como Fazer

**Passo 1: Ler a rubrica de avaliação**
```powershell
# Windows: abrir as regras de avaliação em português
Get-Content modes/pt/oferta.md
# Procure por "Blocos A-F" (Bloques A-F)
```

**Passo 2: Copiar descrição de vaga para `jds/vaga.txt`**
```powershell
@'
[Cole a descrição completa da vaga aqui]
'@ | Set-Content jds/vaga.txt
```

**Passo 3: Avaliar manualmente usando os blocos**
Abra `modes/pt/oferta.md` e avalie:
- **Bloco A**: Compatibilidade de skills (1-5)
- **Bloco B**: Alinhamento com carreira (1-5)
- **Bloco C**: Compensação (1-5)
- **Bloco D**: Sinais culturais (1-5)
- **Bloco E**: Bandeiras vermelhas (ajustes negativos)
- **Bloco F**: Pontuação geral

**Passo 4: Gerar relatório de avaliação**
Criar `reports/001-empresa-data-2026-04-08.md`:
```markdown
# Relatório de Avaliação

**URL:** https://example.com/vaga

**Empresa:** Exemplo
**Posição:** Diretor Criativo
**Data:** 2026-04-08

## Pontuação: 4.2/5

### Bloco A: Compatibilidade com CV
- [Sua avaliação de compatibilidade de skills]

### Bloco B: Alinhamento North Star
- [A vaga encaixa nos papéis alvo?]

### Bloco C: Compensação
- Oferecido: R$ 8.000
- Alvo: R$ 8.000-12.000
- Avaliação: 4/5

### Bloco D: Sinais Culturais
- [Avaliação da cultura da empresa]

### Bloco E: Bandeiras Vermelhas
- [Sinais de alerta?]

### Bloco F: Avaliação Global
- Geral: 4.2/5
- Recomendação: Candidatar-se
```

**Passo 5: Adicionar ao rastreador**
Edite `data/applications.md`:
```markdown
| # | Data | Empresa | Posição | Pontuação | Status | PDF | Relatório | Observações |
|---|------|---------|---------|-----------|--------|-----|-----------|-------------|
| 1 | 2026-04-08 | Exemplo | Diretor Criativo | 4.2/5 | Avaliada | ❌ | [001](reports/001-exemplo-2026-04-08.md) | Bom encaixe, compatível com trabalho de marca |
```

---

## Funcionalidade 2: Geração de PDF (Automatizada)

### O Que Fazer
Criar um CV personalizado via HTML e converter para PDF usando o script.

### Como Fazer

**Passo 1: Criar arquivo HTML**
Use `templates/cv-template.html` como base. Substitua os placeholders:
```html
<!-- Em templates/cv-template.html, substitua: -->
{{NAME}} → "Seu Nome"
{{EMAIL}} → "voce@example.com"
{{PORTFOLIO_URL}} → "https://seu-portfolio.exemplo.com"
{{PORTFOLIO_DISPLAY}} → "Portfólio"
{{SUMMARY_TEXT}} → "Diretor criativo com 10+ anos de experiência em comunicação audiovisual..."
{{PORTFOLIO_HIGHLIGHTS}} → HTML de 2-3 projetos principais com métricas
{{COMPETENCIES}} → Tags como <span class="competency-tag">Audiovisual</span>
```

**Passo 2: Salvar como `/tmp/cv-custom.html`**
```powershell
notepad /tmp/cv-custom.html
# Cole seu HTML personalizado e salve
```

**Passo 3: Gerar PDF**
```powershell
node generate-pdf.mjs /tmp/cv-custom.html output/cv-example-2026-04-08.pdf --format=a4
```

**Passo 4: Verificar**
Verifique se o PDF foi criado:
```powershell
Get-Item output/cv-*.pdf
```

### Exemplo: Personalizar para Papel de Marca/Campanha
Edite o resumo para destacar realizações de campanha:

```html
{{SUMMARY_TEXT}} → 
"Diretor cinematográfico especializado em campanhas de marca. 
Liderou produção de conteúdo que alcançou 2M+ visualizações e 
aumento de 40% no reconhecimento de marca. Experiência em 
direção, produção audiovisual e comunicação corporativa."
```

---

## Funcionalidade 3: Rastreamento de Portais (Manual)

### O Que Fazer
Verificar portais de empregos e rastrear novas oportunidades.

### Como Fazer

**Passo 1: Editar consultas de busca em `portals.yml`**
O arquivo já tem filtros de papéis criativos para:
- LinkedIn Brasil
- Vagas.com.br
- Catho
- Indeed Brasil
- Behance
- Dribbble

**Passo 2: Verificar manualmente ou adicionar ao pipeline**
Edite `data/pipeline.md` com novas URLs:
```markdown
# Pipeline - URLs Pendentes

- https://www.linkedin.com/jobs/view/123456789
- https://job-board.com/creative-director-rio
- https://vagas.com.br/vaga/12345
```

**Passo 3: Mover para candidaturas com avaliação**
Uma vez avaliada, mova a URL de pipeline.md para applications.md com status.

---

## Funcionalidade 4: Gerenciamento de Rastreador em Lote (Scripts)

### Mesclar adições de rastreador
Se você criar arquivos TSV em `batch/tracker-additions/`:
```powershell
node merge-tracker.mjs
```

### Verificar integridade do rastreador
```powershell
node verify-pipeline.mjs
```

### Normalizar statuses
```powershell
node normalize-statuses.mjs
```

### Remover duplicatas
```powershell
node dedup-tracker.mjs
```

---

## Funcionalidade 5: Verificação de Saúde do Sistema

### Auxiliar de diagnóstico
```powershell
node doctor.mjs
```

Verifica:
- Se arquivos obrigatórios existem
- Se fontes estão no lugar
- Se arquivos de config são válidos
- Se Node.js e Playwright estão configurados

### Verificar atualizações
```powershell
node update-system.mjs check
```

---

## Funcionalidade 6: Personalização de Currículo Criativo (Com Sua Configuração)

### Perfil personalizado
Edite `config/profile.yml`:
```yaml
candidate:
  full_name: "Seu Nome"
  email: "voce@example.com"
  portfolio_url: "https://seu-portfolio.exemplo.com/"
  
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

### Fluxo de CV de exemplo
1. Criar `cv-custom.md` com currículo completo
2. Criar `article-digest.md` com projetos de portfólio
3. Para cada vaga, copie `templates/cv-template.html`
4. Edite placeholders com keywords específicas da vaga
5. Execute `node generate-pdf.mjs` para gerar PDF
6. Rastreie em `data/applications.md`

---

## Exemplo de Fluxo Completo

### Cenário: Candidatar-se a vaga de Diretor Criativo no Rio

**1. Encontrar a vaga**
- Salve URL em `data/pipeline.md`
- Leia o JD completo

**2. Avaliar**
- Abra `modes/pt/oferta.md`
- Leia os blocos (pontuação A-F)
- Pontuação: 4.3/5 → Recomendação: Candidatar-se

**3. Criar relatório de avaliação**
- Criar `reports/001-empresa-rio-2026-04-08.md`
- Execute: `Get-Content modes/pt/oferta.md > reports/001-empresa-rio-2026-04-08.md`
- Adicione suas pontuações manuais

**4. Personalizar CV**
- Abra `templates/cv-template.html` no editor
- Substitua placeholders `{{...}}`:
  - Nome, email, portfólio
  - Resumo: "Diretor com expertise em campanhas..."
  - Destaques de Portfólio: 2-3 projetos de trabalho de marca/Rio
  - Competências: Diretor Criativo, Audiovisual, Estratégia de Marca
  - Experiência: Reordene bullets por relevância
- Salve em `/tmp/cv-custom.html`

**5. Gerar PDF**
```powershell
node generate-pdf.mjs /tmp/cv-custom.html output/cv-example-2026-04-08.pdf --format=a4
```

**6. Rastrear**
Edite `data/applications.md`:
```markdown
| 1 | 2026-04-08 | Empresa Rio | Diretor Criativo | 4.3/5 | Candidatura Enviada | ✅ | [001](reports/001-empresa-rio-2026-04-08.md) | Bom encaixe, candidatura enviada 04-08 |
```

**7. Gerenciar**
- Mantenha relatórios organizados em `reports/`
- Atualize status quando empresa responder
- Mude para "Entrevista", "Oferta", "Rejeitada", etc.

---

## Dicas de Integração com Codex

Você tem **Codex** (conclusão de código do ChatGPT). Use-o para:

1. **Escrever personalizações de HTML**
   - Codex ajudará você a formatar o template do CV
   - Peça ao Codex para gerar rótulos de seção em PT-BR
   - Gere pontos de bala criativos para experiência

2. **Editar modos para lógica personalizada**
   - Modifique `modes/_shared.md` pontuação de arquétipos
   - Atualize `modes/pt/_profile.md` com narrativa personalizada

3. **Criar scripts auxiliares**
   - Peça ao Codex para escrever um script PowerShell que automatize etapas
   - Gere processadores em lote para avaliações

4. **Escrever cartas de apresentação**
   - Use Codex para rascunhar cartas de apresentação em PT-BR ou EN
   - Personalize usando keywords da descrição de vaga

---

## Resumo

| Funcionalidade | Como Usar |
|----------------|-----------|
| **Avaliação de Vagas** | Pontuação manual usando rubrica `modes/pt/oferta.md` |
| **Geração de PDF** | Edite template HTML + execute `node generate-pdf.mjs` |
| **Rastreamento de Portais** | Atualize `portals.yml` + verifique manualmente ou WebSearch |
| **Gerenciamento de Rastreador** | Edite `data/applications.md` + execute scripts merge/verify |
| **Saúde do Sistema** | Execute `node doctor.mjs` e `node update-system.mjs check` |
| **Currículos Personalizados** | Edite HTML, injete keywords, gere com Node.js |
| **Ajuda de Código** | Use Codex para escrita/edição |

---

## Próximos Passos

1. **Instale Node.js** agora se ainda não o fez
2. **Execute `node doctor.mjs`** para verificar configuração
3. **Teste geração de PDF** com um arquivo HTML simples
4. **Crie sua primeira avaliação** manualmente
5. **Gere um CV personalizado** para uma vaga de teste

Você pode fazer **tudo** manualmente pelo terminal, sem precisar de um agente de chat. É mais trabalho, mas totalmente funcional!

Dúvidas? Confira `README.md` ou `docs/SETUP.md` para mais detalhes.
