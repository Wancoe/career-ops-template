# Modo: pdf — Geração de PDF ATS-otimizado

## Pipeline completo

1. Leia `cv.md` como fonte de verdade.
2. Peça ao usuário a descrição da vaga se não estiver no contexto (texto ou URL).
3. Extraia 15-20 keywords da vaga.
4. Detecte o idioma da vaga → idioma do CV (PT-BR se a vaga estiver em português, EN se estiver em inglês).
5. Detecte a localização da empresa → formato papel:
   - US/Canada → `letter`
   - Resto do mundo → `a4`
6. Detecte o arquétipo do cargo e adapte o tom para criativo/audiovisual.
7. Reescreva o resumo profissional injetando keywords da vaga + ponte narrativa relevante.
8. Selecione 2-3 destaques de portfólio (projetos, campanhas, cases de marca, conteúdo ou produção audiovisual) com métricas e links.
9. Selecione os 3-4 projetos mais relevantes para a vaga.
10. Reordene os bullets de experiência por relevância à vaga.
11. Construa a grade de competências a partir dos requisitos do JD (6-8 frases-chave).
12. Injete keywords de forma natural nos resultados existentes (NUNCA invente).
13. Gere o HTML completo a partir de `templates/cv-template.html` com conteúdo personalizado.
14. Escreva o HTML em `/tmp/cv-candidate-{company}.html`.
15. Execute: `node generate-pdf.mjs /tmp/cv-candidate-{company}.html output/cv-candidate-{company}-{YYYY-MM-DD}.pdf --format={letter|a4}`
16. Reporte: caminho do PDF, número de páginas, cobertura de keywords.

## Regras ATS (parseo limpo)

- Layout single-column (sem colunas paralelas ou sidebars).
- Seções padrão: "Professional Summary" / "Resumo Profissional", "Work Experience" / "Experiência", "Education" / "Formação", "Skills" / "Competências", "Certifications" / "Certificações", "Projects" / "Projetos".
- Não use texto em imagens ou SVGs.
- Não coloque informação crítica em headers/footers.
- UTF-8, texto selecionável (não rasterizado).
- Sem tabelas aninhadas.
- Distribua keywords do JD: summary, primeiro bullet de cada cargo, seção de skills.
- Use linguagem clara e criativa: fale de marcas, campanhas, audiência, engajamento, conversão e reconhecimento.
- Evite jargões técnicos de engenharia quando não são necessários.
- Priorize resultados simples e mensuráveis: "Aumentou alcance orgânico 40%", "Campanha com 2M visualizações".
- Frases curtas e diretas; evite abstrações vazias.

## Design do PDF

- **Fonts**: Space Grotesk (títulos) + DM Sans (corpo).
- **Fonts self-hosted**: `fonts/`.
- **Header**: nome grande + linha gradiente + contatos + link de portfólio.
- **Section headers**: Space Grotesk 13px, uppercase, cor primária cyan.
- **Body**: DM Sans 11px, line-height 1.5.
- **Company names**: cor de destaque roxa.
- **Margens**: 0.6in.
- **Fundo**: branco.

## Ordem de seções

1. Header (nome, gradiente, contato, link de portfólio)
2. Professional Summary / Resumo Profissional (3-4 linhas, denso em keywords)
3. Portfolio Highlights / Destaques do Portfólio (2-3 cases, campanhas, métricas, links)
4. Core Competencies / Competências Core (6-8 frases-chave)
5. Work Experience / Experiência
6. Projects / Projetos
7. Education & Certifications / Formação e Certificações
8. Skills / Competências

## Template HTML

Use o template em `templates/cv-template.html`. Substitua os placeholders `{{...}}` com conteúdo personalizado:

| Placeholder | Conteúdo |
|-------------|----------|
| `{{LANG}}` | `en` ou `es` |
| `{{PAGE_WIDTH}}` | `8.5in` (letter) ou `210mm` (A4) |
| `{{NAME}}` | (de `profile.yml`) |
| `{{EMAIL}}` | (de `profile.yml`) |
| `{{LINKEDIN_URL}}` | (de `profile.yml`) |
| `{{LINKEDIN_DISPLAY}}` | (de `profile.yml`) |
| `{{PORTFOLIO_URL}}` | (de `profile.yml`) |
| `{{PORTFOLIO_DISPLAY}}` | (de `profile.yml`) |
| `{{LOCATION}}` | (de `profile.yml`) |
| `{{SECTION_SUMMARY}}` | Professional Summary / Resumo Profissional |
| `{{SUMMARY_TEXT}}` | Summary personalizado com keywords |
| `{{SECTION_PORTFOLIO}}` | Portfolio Highlights / Destaques do Portfólio |
| `{{PORTFOLIO_HIGHLIGHTS}}` | Lista de 2-3 projetos chave com impacto, métricas e links |
| `{{SECTION_COMPETENCIES}}` | Core Competencies / Competências Core |
| `{{COMPETENCIES}}` | `<span class="competency-tag">keyword</span>` × 6-8 |
| `{{SECTION_EXPERIENCE}}` | Work Experience / Experiência |
| `{{EXPERIENCE}}` | HTML de cada cargo com bullets |
| `{{SECTION_PROJECTS}}` | Projects / Projetos |
| `{{PROJECTS}}` | HTML de top 3-4 projetos |
| `{{SECTION_EDUCATION}}` | Education / Formação |
| `{{EDUCATION}}` | HTML de educação |
| `{{SECTION_CERTIFICATIONS}}` | Certifications / Certificações |
| `{{CERTIFICATIONS}}` | HTML de certificações |
| `{{SECTION_SKILLS}}` | Skills / Competências |
| `{{SKILLS}}` | HTML de habilidades |

## Canva CV (opcional)

Se `config/profile.yml` tiver `canva_resume_design_id`, ofereça a escolha:
- **HTML/PDF (rápido, ATS-otimizado)**
- **Canva CV (visual, preserva o design)**

Se não houver `canva_resume_design_id`, use o fluxo HTML/PDF.

## Pós-geração

Atualize o tracker se a vaga já existir: troque o PDF de ❌ para ✅ quando o documento estiver pronto.
