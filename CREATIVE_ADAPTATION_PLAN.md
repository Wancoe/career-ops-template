# Career-Ops Adaptation Plan: Creative Jobs in Brazil

## Overview
Adapt the career-ops repository to support non-tech creative job searches for clients based in Brazil. The system will maintain its core structure while shifting focus from AI/tech roles to creative professions.

## Key Changes Required

### 1. Language Configuration
- **Default Language**: Set Portuguese (Brazilian) as the primary language
- **Mode Directory**: Use `modes/pt/` for all evaluations and processing
- **Update**: `config/profile.example.yml` to include `language.modes_dir: modes/pt`

### 2. Archetype Updates
**File**: `modes/_shared.md`
- Replace AI/tech archetypes with creative roles:
  - Graphic Designer / Designer Gráfico
  - Content Creator / Criador de Conteúdo
  - Marketing Specialist / Especialista em Marketing
  - UX/UI Designer / Designer UX/UI
  - Art Director / Diretor de Arte
  - Copywriter / Redator
  - Social Media Manager / Gerente de Mídias Sociais
  - Digital Artist / Artista Digital
  - Brand Manager / Gerente de Marca
  - Creative Director / Diretor Criativo

**Adaptive Framing Table**: Update to map creative projects to these archetypes

### 3. Profile Configuration
**File**: `config/profile.example.yml`
- **target_roles**: Update examples to creative positions
- **narrative**: Adjust headline and superpowers for creative fields
- **proof_points**: Include creative portfolio examples
- **location**: Set Brazil as default
- **compensation**: Adjust ranges for Brazilian creative market
- **visa_status**: Update for Brazilian context

### 4. Portal Scanner Configuration
**File**: `templates/portals.example.yml`
- **title_filter.positive**: Replace tech keywords with creative ones:
  - "Designer", "Criativo", "Marketing", "Conteúdo", "Arte", "Branding", "Social Media", "UX", "UI", "Copywriter", "Redator", "Artista Digital"
- **tracked_companies**: Add Brazilian companies and creative agencies:
  - Local advertising agencies (DPZ, Africa, WMcCann)
  - Tech companies with creative roles (Nubank, iFood, Stone)
  - Media companies (Globo, Editora Abril)
  - Creative platforms (99designs, Behance jobs)
- **search_queries**: Update with Brazilian job sites:
  - Vagas.com, Catho, Indeed Brazil
  - LinkedIn Brazil
  - Creative-specific: Behance, Dribbble job boards

### 5. CV Template Adjustments
**File**: `templates/cv-template.html`
- **Portfolio Integration**: Add prominent portfolio section for creative work
- **Visual Elements**: Enhance design elements suitable for creative CVs
- **Brazilian Formatting**: Adjust for Brazilian CV conventions (optional photo, different section ordering)

### 6. Scoring System Adaptation
**File**: `modes/_shared.md`
- **Dimensions**: Adapt evaluation criteria for creative roles:
  - Portfolio quality over technical certifications
  - Creative problem-solving over algorithmic thinking
  - Brand impact over system performance
  - Visual communication skills over code quality

### 7. Negotiation Scripts
**File**: `modes/_profile.md` (via customization)
- **Brazilian Context**: Include CLT vs PJ discussions
- **Benefits**: Vale-refeição, plano de saúde, férias, 13º salário
- **Creative Compensation**: Portfolio rates, project-based pay, royalties

### 8. Portuguese Mode Enhancements
**Files**: `modes/pt/*.md`
- **Archetypes**: Translate and adapt creative archetypes
- **Brazilian Market**: Enhance with local creative industry knowledge
- **Cultural Context**: Include Brazilian business culture notes

### 9. Documentation Updates
**Files**: `README.md`, `docs/SETUP.md`, `docs/CUSTOMIZATION.md`
- Update examples to show creative roles instead of tech
- Include Brazilian job market context
- Add creative portfolio setup instructions

### 10. Example Files
**Files**: `examples/cv-example.md`, `examples/article-digest-example.md`
- Replace with creative CV and portfolio examples
- Include Brazilian creative professional examples

## Implementation Steps

1. **Language Setup**: Configure Portuguese as default mode
2. **Archetype Migration**: Update core archetypes in _shared.md
3. **Profile Templates**: Modify example configurations
4. **Portal Configuration**: Add Brazilian creative job sources
5. **Template Updates**: Enhance CV template for creative portfolios
6. **Scoring Calibration**: Adjust evaluation criteria
7. **Documentation**: Update all docs with creative examples
8. **Testing**: Validate with sample creative job descriptions

## Preservation Strategy
- Maintain all existing functionality
- Keep file-based, local operation
- Preserve multi-language support
- Retain batch processing and automation features
- Keep ATS-optimized PDF generation
- Maintain pipeline integrity and tracking

## Client Onboarding
For Brazilian creative clients:
1. Use Portuguese interface
2. Focus on portfolio showcase
3. Include local market compensation data
4. Emphasize creative problem-solving in evaluations
5. Customize for Brazilian business culture

## Validation
After implementation:
- Test evaluation with sample creative job posting
- Verify PDF generation with portfolio content
- Confirm portal scanning finds relevant creative roles
- Ensure Portuguese language support throughout</content>
<parameter name="filePath">c:\Users\Wanderson\career-ops\CREATIVE_ADAPTATION_PLAN.md