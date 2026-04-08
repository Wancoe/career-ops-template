# Guia Simples: Como Usar Career-Ops (Sem Comandos Técnicos)

**Olá!** Este guia mostra como usar o sistema Career-Ops sem precisar digitar comandos no computador. Tudo pode ser feito com arquivos e pastas no Windows.

---

## 📋 O Que É Career-Ops?

Career-Ops é um sistema que ajuda você a:
- **Avaliar vagas** de diretor cinematográfico e produtor audiovisual
- **Criar currículos personalizados** para cada vaga
- **Organizar suas candidaturas** em uma tabela simples
- **Mostrar seu portfólio** de forma profissional

Você não precisa ser técnico — apenas seguir estes passos!

---

## 🚀 Passo 1: Preparar Seu Computador (15 minutos)

### A. Instalar Node.js
1. Abra seu navegador (Chrome, Edge, etc.)
2. Vá para: **https://nodejs.org/**
3. Clique no botão verde **"Download Node.js (LTS)"**
4. Baixe o arquivo `.msi` (cerca de 30MB)
5. **Clique duas vezes** no arquivo baixado para instalar
6. Siga as instruções na tela (clique "Next" várias vezes)
7. Quando terminar, clique "Finish"

**Verificar se funcionou:**
- Abra o Explorador de Arquivos
- Clique com botão direito na área vazia
- Escolha "Abrir janela do PowerShell aqui" ou "Abrir terminal aqui"
- Digite: `node --version`
- Deve aparecer algo como "v18.17.0" ou similar

### B. Baixar Playwright (para PDFs)
1. Abra o terminal novamente (como acima)
2. Digite: `npx playwright install chromium`
3. Espere baixar (pode levar alguns minutos)
4. Quando terminar, feche o terminal

---

## 📁 Passo 2: Organizar Seus Arquivos (10 minutos)

### A. Criar Estrutura de Pastas
1. Abra **Explorador de Arquivos**
2. Vá para a pasta `career-ops` (onde você baixou o projeto)
3. Clique com botão direito na área vazia
4. Escolha **"Novo" → "Pasta"** e crie estas pastas:
   - `output`
   - `reports`
   - `jds`
   - `batch/tracker-additions`

### B. Copiar Arquivos de Exemplo
1. Na pasta `career-ops`, encontre `config/profile.example.yml`
2. Clique com botão direito → **"Copiar"**
3. Cole na mesma pasta e renomeie para `profile.yml`

4. Faça o mesmo com `templates/portals.example.yml`:
   - Copie e renomeie para `portals.yml`

### C. Criar Seus Arquivos Pessoais
1. Clique com botão direito na pasta `career-ops`
2. **"Novo" → "Documento de Texto"** e crie:
   - `cv.md` (seu currículo completo)
   - `article-digest.md` (seus projetos de portfólio)
   - `data/applications.md` (rastreamento de candidaturas)
   - `data/pipeline.md` (vagas para avaliar)

---

## ✏️ Passo 3: Configurar Seus Dados (20 minutos)

### A. Editar Seu Perfil
1. Abra `config/profile.yml` com **Bloco de Notas**
2. Substitua os dados de exemplo pelos seus:

```yaml
candidate:
  full_name: "Seu Nome"
  email: "voce@example.com"
  phone: "+55-11-99999-9999"
  location: "Sua Cidade, Estado"
  linkedin: "linkedin.com/in/seu-perfil"
  portfolio_url: "https://seu-portfolio.exemplo.com"
  github: "github.com/seu-usuario"
```

3. Salve e feche

### B. Escrever Seu Currículo
1. Abra `cv.md` com Bloco de Notas
2. Escreva seu currículo em formato simples:

```markdown
# Seu Nome

## Resumo Profissional
Diretor cinematográfico com 10+ anos criando conteúdo impactante para marcas.

## Experiência
### Diretor Cinematográfico - Empresa X (2020-2024)
- Dirigi campanhas publicitárias que alcançaram 2M+ visualizações
- Produzi conteúdo audiovisual para comunicação corporativa
- Liderou equipe de produção de vídeo

### Produtor Audiovisual - Empresa Y (2015-2020)
- Coordenou produção de documentários e comerciais
- Gerenciou orçamentos de projetos audiovisuais
- Desenvolveu estratégias de conteúdo digital
```

3. Salve e feche

### C. Adicionar Seu Portfólio
1. Abra `article-digest.md` com Bloco de Notas
2. Liste seus projetos principais:

```markdown
# Projetos de Portfólio

## Campanha "Marca X" (2024)
- **Descrição:** Direção cinematográfica de campanha publicitária
- **Resultado:** 2M+ visualizações, 95% engajamento
- **Link:** https://portfolio.com/campaign

## Vídeo Institucional Y (2023)
- **Descrição:** Produção audiovisual corporativa
- **Resultado:** Redução de 60% na rotatividade de funcionários
- **Link:** https://portfolio.com/video

## Projeto de Comunicação Interna Z (2022)
- **Descrição:** Estratégia de comunicação corporativa
- **Resultado:** Aumento de 40% no reconhecimento da marca
- **Link:** https://portfolio.com/comunicacao
```

3. Salve e feche

---

## 📊 Passo 4: Criar Sistema de Rastreamento (10 minutos)

### A. Configurar Tabela de Candidaturas
1. Abra `data/applications.md` com Bloco de Notas
2. Cole este cabeçalho:

```markdown
# Rastreamento de Candidaturas

| # | Data | Empresa | Posição | Pontuação | Status | PDF | Relatório | Observações |
|---|------|---------|---------|-----------|--------|-----|-----------|-------------|
```

3. Salve e feche

### B. Configurar Lista de Vagas Pendentes
1. Abra `data/pipeline.md` com Bloco de Notas
2. Cole este cabeçalho:

```markdown
# Vagas para Avaliar

- https://www.linkedin.com/jobs/view/123456789
- https://vagas.com.br/vaga/12345
```

3. Salve e feche

---

## 🔍 Passo 5: Como Avaliar uma Vaga (15 minutos por vaga)

### A. Salvar a Descrição da Vaga
1. Abra seu navegador e encontre uma vaga interessante
2. Copie toda a descrição da vaga
3. Abra `jds/` pasta
4. Clique com botão direito → **"Novo" → "Documento de Texto"**
5. Nomeie como `vaga-01-empresa.txt`
6. Cole a descrição completa
7. Salve e feche

### B. Avaliar a Vaga (Pontuação Manual)
1. Abra `modes/pt/oferta.md` com Bloco de Notas
2. Leia as regras dos **Blocos A-F**
3. Para cada bloco, dê uma nota de 1-5:
   - **Bloco A:** Suas habilidades combinam? (1-5)
   - **Bloco B:** A vaga combina com seus objetivos? (1-5)
   - **Bloco C:** O salário está bom? (1-5)
   - **Bloco D:** A empresa parece boa? (1-5)
   - **Bloco E:** Há problemas? (pontos negativos)
   - **Bloco F:** Pontuação geral (média dos outros)

### C. Criar Relatório de Avaliação
1. Vá para pasta `reports/`
2. Clique com botão direito → **"Novo" → "Documento de Texto"**
3. Nomeie como `001-empresa-2026-04-08.md`
4. Cole este template e preencha:

```markdown
# Relatório de Avaliação

**URL:** [cole o link da vaga aqui]

**Empresa:** [nome da empresa]
**Posição:** [título da vaga]
**Data:** 2026-04-08

## Pontuação: [sua pontuação]/5

### Bloco A: Compatibilidade com CV
- [explique se suas habilidades combinam]

### Bloco B: Alinhamento North Star
- [a vaga combina com diretor cinematográfico/produtor?]

### Bloco C: Compensação
- Oferecido: [salário oferecido]
- Seu alvo: R$ 8.000-12.000
- Avaliação: [nota]/5

### Bloco D: Sinais Culturais
- [a empresa parece boa? Cultura, benefícios, etc.]

### Bloco E: Bandeiras Vermelhas
- [há problemas? Salário baixo, empresa ruim, etc.]

### Bloco F: Avaliação Global
- Geral: [pontuação]/5
- Recomendação: [Candidatar-se / Não candidatar / Considerar se...]
```

5. Salve e feche

### D. Adicionar à Tabela de Candidaturas
1. Abra `data/applications.md`
2. Adicione uma linha no final:

```
| 1 | 2026-04-08 | Empresa | Diretor Criativo | 4.2/5 | Avaliada | ❌ | [001](reports/001-empresa-2026-04-08.md) | Bom encaixe, combina com campanhas |
```

3. Salve e feche

---

## 📄 Passo 6: Criar Currículo Personalizado (20 minutos por vaga)

### A. Preparar Arquivo HTML
1. Abra `templates/cv-template.html` com Bloco de Notas
2. Este é o template do seu currículo
3. Você vai editar os códigos entre `{{ }}` para personalizar

### B. Personalizar para a Vaga
Substitua estes códigos:

**Nome e Contato:**
```
{{NAME}} → Seu Nome
{{EMAIL}} → voce@example.com
{{PORTFOLIO_URL}} → https://seu-portfolio.exemplo.com
{{LOCATION}} → Rio de Janeiro, RJ
```

**Resumo Profissional:**
```
{{SUMMARY_TEXT}} →
Diretor cinematográfico com 10+ anos criando conteúdo impactante.
Especialista em campanhas publicitárias e produção audiovisual.
Experiência em direção de projetos que alcançaram milhões de visualizações.
```

**Destaques de Portfólio:**
```
{{PORTFOLIO_HIGHLIGHTS}} →
<li class="portfolio-item">
  <strong>Campanha "Marca X" (2024)</strong> — Direção cinematográfica, 2M+ visualizações,
  95% engajamento. <a href="https://portfolio.com/campaign">Ver projeto</a>
</li>
<li class="portfolio-item">
  <strong>Vídeo Institucional Y (2023)</strong> — Produção audiovisual corporativa,
  redução de rotatividade 60%. <a href="https://portfolio.com/video">Ver projeto</a>
</li>
```

**Competências:**
```
{{COMPETENCIES}} →
<span class="competency-tag">Direção Cinematográfica</span>
<span class="competency-tag">Produção Audiovisual</span>
<span class="competency-tag">Motion Design</span>
<span class="competency-tag">Estratégia de Marca</span>
<span class="competency-tag">Storytelling</span>
<span class="competency-tag">Comunicação Corporativa</span>
```

### C. Salvar Versão Personalizada
1. Clique **"Arquivo" → "Salvar Como"**
2. Salve na pasta `output/` como `cv-custom.html`
3. Salve e feche

### D. Gerar PDF
1. Abra o terminal (Explorador de Arquivos → botão direito → "Abrir PowerShell aqui")
2. Digite este comando exatamente:
```
node generate-pdf.mjs output/cv-custom.html output/cv-example-2026-04-08.pdf --format=a4
```
3. Pressione Enter
4. Espere aparecer "PDF generated"
5. Verifique na pasta `output/` — deve ter um arquivo `.pdf`

---

## 📋 Passo 7: Gerenciar Suas Candidaturas

### Atualizar Status
1. Abra `data/applications.md`
2. Mude o status conforme avança:
   - `Avaliada` → quando terminar relatório
   - `Candidatura Enviada` → quando enviar currículo
   - `Entrevista` → quando agendada
   - `Oferta` → quando receber proposta
   - `Rejeitada` → quando empresa disser não

### Exemplo de Linha Completa:
```
| 1 | 2026-04-08 | Empresa X | Diretor Criativo | 4.3/5 | Candidatura Enviada | ✅ | [001](reports/001-empresa-x-2026-04-08.md) | Enviado 04-08, aguardando resposta |
```

---

## 🎯 Dicas para Usar Bem

### Para Vagas de Diretor Cinematográfico:
- Foque em campanhas publicitárias, direção de cena, produção audiovisual
- Destaque métricas: visualizações, engajamento, reconhecimento de marca
- Mostre experiência com equipes e orçamentos

### Para Vagas de Produtor Audiovisual:
- Enfatize coordenação, orçamento, planejamento
- Mostre projetos completos do início ao fim
- Inclua comunicação com clientes e equipes

### Quando Personalizar Currículo:
- Leia a descrição da vaga
- Encontre palavras-chave importantes
- Use essas palavras no resumo e experiência
- Mantenha foco no portfólio relevante

### Organização:
- Mantenha `cv.md` sempre atualizado
- Adicione novos projetos em `article-digest.md`
- Use `data/pipeline.md` para vagas que quer avaliar depois
- Arquive PDFs em `output/` por empresa/data

---

## ❓ Quando Pedir Ajuda

Se algo não funcionar:
1. Verifique se Node.js está instalado (abra terminal, digite `node --version`)
2. Certifique-se que salvou todos os arquivos
3. Leia as mensagens de erro no terminal
4. Peça ajuda para alguém técnico se necessário

---

## ✅ Checklist de Verificação

Antes de começar:
- [ ] Node.js instalado
- [ ] Playwright instalado
- [ ] Pastas criadas (output, reports, jds, batch/tracker-additions)
- [ ] Arquivos copiados (profile.yml, portals.yml)
- [ ] Dados pessoais configurados
- [ ] Currículo escrito em cv.md
- [ ] Portfólio em article-digest.md
- [ ] Tabelas de rastreamento criadas

Pronto! Agora você pode avaliar vagas e criar currículos personalizados sem precisar ser técnico. Comece testando com uma vaga que você gosta! 🚀
