# Relatório Parcial — Preenchimento Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preencher completamente o Relatório Parcial do Projeto Integrador III (UNIVESP) com conteúdo real do projeto Leciona, seguindo normas ABNT.

**Architecture:** O relatório é um documento LaTeX modular (`docs/partial-report/`) com um arquivo principal (`main.tex`) que importa seções de `content/`. Cada tarefa edita um ou mais arquivos `.tex` com conteúdo acadêmico baseado nos dados do Plano de Ação (PDF entregue) e do codebase Django.

**Tech Stack:** LaTeX, pacote customizado `univesp-abnt.sty`, formatação ABNT

---

## Dados de referência (extraídos do Plano de Ação e codebase)

### Integrantes
- Allan Di Pace Schmidt (RA 23203894)
- Alysson Alcantara (RA 23211184)
- Anderson de Souza Pereira (RA 23212113)
- Mariana Luisa de Faria Santos (RA 123123)
- Guilherme Cardoso de Almeida (RA 23206504)
- Whedja Silva Cavalcante (RA 23220169)

### Projeto
- **Título:** Leciona: Plataforma Cloud de Gestão Escolar e API
- **Curso:** Bacharelado em Tecnologia da Informação
- **Disciplina:** Projeto Integrador em Computação III
- **Orientadora:** Laís de Ponte
- **Polo:** Cachoeira Paulista / São Sebastião
- **Cidade:** São Sebastião
- **Ano:** 2026
- **Escola parceira:** Escola Municipal Patrícia Viviani (Topolândia, São Sebastião - SP)
- **Contato na escola:** Vice-Diretora Marília Izabel

### Stack Técnica
- Python 3.10+, Django 5.2, PostgreSQL 15
- Docker + Docker Compose, Gunicorn, WhiteNoise
- Chart.js 4.x, Jazzmin (AdminLTE/Bootstrap)
- ReportLab (PDF), Faker (seed data)
- Terraform (IaC placeholder)
- GitHub Actions (CI/CD planejado)

### Módulos do Sistema
1. **core** — Professores, Disciplinas, Turmas, Segmentos, Períodos, Justificativas
2. **schedule** — Grade de horários com UniqueConstraints
3. **attendance** — Ausências e substituições com validações
4. **communication** — Mensagens categorizadas para turmas/professores

---

## Task 1: Metadados do documento (`main.tex`)

**Files:**
- Modify: `docs/partial-report/main.tex:14-22`

- [ ] **Step 1: Preencher os \newcommand com dados reais**

Substituir os placeholders pelos valores corretos:

```latex
\newcommand{\doctitulo}{Leciona: Plataforma Cloud de Gestão Escolar e API}
\newcommand{\docautores}{Allan Di Pace Schmidt \\ Alysson Alcantara \\ Anderson de Souza Pereira \\ Guilherme Cardoso de Almeida \\ Mariana Luisa de Faria Santos \\ Whedja Silva Cavalcante}
\newcommand{\doccidade}{São Sebastião}
\newcommand{\docano}{2026}
\newcommand{\doccurso}{Bacharelado em Tecnologia da Informação}
\newcommand{\doctutor}{Laís de Ponte}
\newcommand{\docpolo}{Cachoeira Paulista / São Sebastião}
\newcommand{\docpaginas}{00}
\newcommand{\docpalavraschave}{Gestão escolar; Django; API RESTful; Computação em nuvem; Integração contínua}
```

> Nota: `\docpaginas` será atualizado na Task final após compilar o PDF.

- [ ] **Step 2: Remover textos de instrução da capa e folha de rosto**

Em `content/capa.tex`, remover as linhas de instrução como "(Fonte: Arial ou Times 14)" etc.
Em `content/folha-rosto.tex`, remover as instruções e trocar "Ano" por `\docano`.

- [ ] **Step 3: Compilar e verificar capa + folha de rosto**

```bash
cd docs && make partial-report
```

Verificar no PDF que capa e folha de rosto exibem os dados corretos.

---

## Task 2: Ficha catalográfica e Resumo (`ficha-resumo.tex`)

**Files:**
- Modify: `docs/partial-report/content/ficha-resumo.tex`

- [ ] **Step 1: Preencher nomes no formato ABNT**

Formato: SOBRENOME, Prenomes (ordem alfabética por sobrenome)

```
ALCANTARA, Alysson; ALMEIDA, Guilherme Cardoso de; CAVALCANTE, Whedja Silva;
PEREIRA, Anderson de Souza; SANTOS, Mariana Luisa de Faria; SCHMIDT, Allan Di Pace.
```

- [ ] **Step 2: Escrever o resumo (até 250 palavras)**

Conteúdo do resumo deve cobrir:
- Contexto: gestão escolar na rede pública municipal
- Problema: dificuldade no gerenciamento de ausências e substituições de professores
- Objetivo: evoluir o sistema Leciona com nuvem, testes e API
- Metodologia: Design Thinking (ouvir, criar, implementar) em parceria com a Escola Municipal Patrícia Viviani
- Resultados parciais: sistema Django modular com 4 apps, dashboard analítico, export PDF, Docker
- Considerações: solução funcional validada pela comunidade escolar

- [ ] **Step 3: Atualizar polo e ano na ficha**

Trocar "Polo...\docpolo, 2021" para usar `\docpolo, \docano`.

- [ ] **Step 4: Compilar e verificar**

---

## Task 3: Introdução (`introducao.tex`)

**Files:**
- Modify: `docs/partial-report/content/introducao.tex`

- [ ] **Step 1: Reescrever a introdução com conteúdo real**

Substituir todo o conteúdo de instrução pelo texto real. A introdução deve conter ~2 páginas cobrindo:

1. **Contextualização do tema** (~2 parágrafos):
   - A gestão escolar no Brasil enfrenta desafios operacionais diários
   - Ausências de professores são eventos imprevistos que geram cascata de problemas
   - Referência à importância da TI na educação (citar MORAN, 2015 e/ou VALENTE, 2018)

2. **Apresentação do problema** (~2 parágrafos):
   - A Escola Municipal Patrícia Viviani (Topolândia, São Sebastião - SP) enfrenta dificuldades na gestão manual de substituições
   - O controle manual em planilhas/papel é lento, sujeito a erros e não garante integridade (choque de horários)
   - Protótipo anterior (PI2) existia mas carecia de estabilidade em nuvem e API

3. **Motivação e delimitação** (~2 parágrafos):
   - Continuidade da parceria com a escola do PI anterior
   - Necessidade de evolução: deploy em nuvem, testes automatizados, API RESTful
   - Tema norteador da UNIVESP: desenvolvimento web com banco de dados, JavaScript, CI/CD, nuvem, acessibilidade

4. **Objeto do trabalho** (~1 parágrafo):
   - Este trabalho tem como objeto o desenvolvimento e evolução do sistema web "Leciona"
   - Plataforma cloud de gestão escolar com foco em ausências, substituições, grade de horários e comunicação

> Incluir ao menos 2-3 citações indiretas (AUTOR, ano) ao longo do texto.

---

## Task 4: Objetivos (`desenvolvimento.tex` — seção 2.1)

**Files:**
- Modify: `docs/partial-report/content/desenvolvimento.tex` (seção OBJETIVOS)

- [ ] **Step 1: Escrever objetivo geral**

> Evoluir o sistema "Leciona" para uma plataforma cloud de gestão escolar com deploy contínuo em nuvem, garantindo a integridade da alocação de horários via testes automatizados e implementando uma API RESTful para descentralização do consumo de dados de horários e faltas por parte dos professores e gestão da escola.

- [ ] **Step 2: Escrever objetivos específicos**

Lista com verbos no infinitivo:
1. Refatorar a arquitetura do sistema em módulos independentes seguindo princípios SOLID
2. Implementar restrições de integridade a nível de banco de dados (UniqueConstraints) para evitar choques de horários
3. Desenvolver um dashboard analítico com gráficos dinâmicos para visualização de indicadores de ausências e substituições
4. Conteinerizar a aplicação utilizando Docker para garantir paridade entre ambientes de desenvolvimento e produção
5. Criar endpoints de API RESTful para consumo de dados de horários e faltas
6. Implementar pipeline de Integração Contínua (CI/CD) via GitHub Actions
7. Desenvolver funcionalidade de exportação de relatórios em formato PDF
8. Validar a solução junto à comunidade escolar parceira (Escola Municipal Patrícia Viviani)

---

## Task 5: Justificativa e delimitação do problema (`desenvolvimento.tex` — seção 2.2)

**Files:**
- Modify: `docs/partial-report/content/desenvolvimento.tex` (seção JUSTIFICATIVA)

- [ ] **Step 1: Escrever a pergunta norteadora**

> "Como garantir a alta disponibilidade, integridade de dados e facilidade de integração na alocação de substituições emergenciais de professores?"

- [ ] **Step 2: Escrever a justificativa (~1.5 páginas)**

Cobrir:
- **Relevância social:** Impacto direto na comunidade escolar de Topolândia — alunos sem aula, professores substitutos sem informação, secretaria sobrecarregada
- **Relevância acadêmica:** Aplicação prática de engenharia de software moderna (SOLID, TDD, CI/CD, Docker, REST) em um cenário real
- **Contribuição para o local:** Sistema gratuito, em nuvem, acessível pela gestão e professores, reduzindo retrabalho manual
- **Continuidade:** Evolução do protótipo do PI anterior, validado pela escola como necessidade real
- **LGPD:** Preocupação com proteção de dados dos professores usando PostgreSQL e boas práticas

---

## Task 6: Fundamentação teórica (`desenvolvimento.tex` — seção 2.3)

**Files:**
- Modify: `docs/partial-report/content/desenvolvimento.tex` (seção FUNDAMENTAÇÃO TEÓRICA)

- [ ] **Step 1: Escrever subseções temáticas (~4-5 páginas)**

Organizar em subseções:

**2.3.1 Gestão escolar e tecnologia da informação**
- Conceito de gestão escolar (LÜCK, 2009)
- Desafios administrativos nas escolas públicas brasileiras
- Papel da TI na modernização da gestão escolar (MORAN, 2015)

**2.3.2 Desenvolvimento web com Django**
- Arquitetura MTV (Model-Template-View) do Django
- Padrão de projeto MVC e sua variante no Django (HOLOVATY; KAPLAN-MOSS, 2009)
- Princípios SOLID aplicados à modularização de software (MARTIN, 2009)

**2.3.3 Banco de dados relacional e integridade de dados**
- Modelo relacional e PostgreSQL (ELMASRI; NAVATHE, 2011)
- Constraints e validações como mecanismo de garantia de integridade
- Indexação de campos para otimização de consultas

**2.3.4 API RESTful e arquitetura orientada a serviços**
- Conceito de REST (FIELDING, 2000)
- Vantagens de APIs para interoperabilidade e consumo descentralizado de dados
- Django REST Framework como ferramenta de implementação

**2.3.5 Computação em nuvem e conteinerização**
- Conceito de cloud computing (MELL; GRANCE, 2011 — NIST)
- Docker e conteinerização como estratégia cloud-native
- Infraestrutura como código (IaC) com Terraform

**2.3.6 Integração contínua e testes automatizados**
- Conceito de CI/CD (HUMBLE; FARLEY, 2010)
- GitHub Actions como plataforma de automação
- Importância de testes unitários na engenharia de software (SOMMERVILLE, 2011)

**2.3.7 Acessibilidade web**
- Diretrizes WCAG e acessibilidade digital (W3C, 2018)
- Responsividade como requisito de acessibilidade (Bootstrap/AdminLTE)

> Cada subseção deve ter ~3-4 parágrafos com citações indiretas ABNT.
> Incluir ao menos 1 citação direta longa (bloco `\begin{citacao}`) em alguma subseção.

---

## Task 7: Metodologia (`desenvolvimento.tex` — seção 2.4)

**Files:**
- Modify: `docs/partial-report/content/desenvolvimento.tex` (seção METODOLOGIA)

- [ ] **Step 1: Escrever a metodologia (~2 páginas)**

Estruturar conforme metodologia UNIVESP (Design Thinking):

**Ouvir e interpretar o contexto:**
- Descrição da Escola Municipal Patrícia Viviani (escola pública municipal em Topolândia, São Sebastião - SP)
- Perfil dos sujeitos: Vice-Diretora Marília Izabel, equipe de secretaria, professores
- Coleta de informações: reuniões presenciais e remotas com a gestão escolar
- Validação do protótipo anterior e levantamento de novas necessidades (estabilidade, nuvem, API)
- Aplicação do TCLE (Termo de Consentimento Livre e Esclarecido) para coleta de dados

**Criar / Prototipar:**
- Análise qualitativa dos problemas relatados pela escola
- Decisão arquitetural: refatoração em 4 módulos (core, schedule, attendance, communication)
- Modelagem do banco de dados com constraints de integridade
- Prototipação do dashboard analítico com Chart.js
- Conteinerização do ambiente com Docker Compose

**Implementar / Testar:**
- Deploy do sistema em ambiente Docker (web + PostgreSQL)
- Implementação de testes unitários para validar regras de negócio
- Apresentação da solução inicial à escola para coleta de feedback (Quinzena 4)
- Iteração sobre o feedback recebido

---

## Task 8: Resultados preliminares (`desenvolvimento.tex` — seção 2.5)

**Files:**
- Modify: `docs/partial-report/content/desenvolvimento.tex` (seção RESULTADOS PRELIMINARES)
- Create: `docs/partial-report/images/` (diretório para figuras)

- [ ] **Step 1: Escrever a descrição dos resultados (~3-4 páginas com figuras)**

Organizar por etapas:

**Ouvir — Levantamento e validação:**
- Resumo do feedback da Vice-Diretora: sistema bem recebido, demanda por confiabilidade e acesso em nuvem
- Tabela com problemas identificados (ausências sem registro, choques de horário, comunicação descentralizada)

**Criar — Arquitetura e modelagem:**
- Descrição da arquitetura modular Django (4 apps)
- Diagrama de módulos do sistema (FIGURA — placeholder para diagrama)
- Modelo de dados com relacionamentos (FIGURA — diagrama ER ou descrição textual)
- Decisões técnicas: PostgreSQL, Docker, Chart.js, Jazzmin

**Implementar — Sistema funcional:**
- Tela de login do painel administrativo (FIGURA — screenshot)
- Dashboard principal com cards de contadores e gráficos (FIGURA — screenshot)
  - Gráfico de linha: histórico de ocorrências nos últimos 6 meses
  - Gráfico de barras: ausências por dia da semana
  - Gráfico de rosca: distribuição de turmas por período
- Tela de gerenciamento de grade de horários (FIGURA — screenshot)
- Tela de registro de ausências e substituições (FIGURA — screenshot)
- Funcionalidade de exportação em PDF (FIGURA — screenshot ou exemplo)
- Docker Compose: ambiente funcional com `docker-compose up`

> **IMPORTANTE:** As figuras precisam ser screenshots reais do sistema.
> O grupo precisará gerar as imagens e salvar em `docs/partial-report/images/`.
> No texto, usar placeholders `\includegraphics` com caminhos para as imagens.

- [ ] **Step 2: Incluir referências a figuras no texto**

Usar formato:
```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{images/dashboard.png}
\caption{Dashboard principal do sistema Leciona}
\label{fig:dashboard}
\end{figure}
```

---

## Task 9: Referências bibliográficas (`referencias.tex`)

**Files:**
- Modify: `docs/partial-report/content/referencias.tex`

- [ ] **Step 1: Substituir referências de exemplo por referências reais**

Lista de referências (ABNT 6023) a incluir:

1. DJANGO SOFTWARE FOUNDATION. **Django documentation.** Version 5.2. 2024. Disponível em: <https://docs.djangoproject.com/en/5.2/>. Acesso em: mar. 2026.

2. DOCKER INC. **Docker Documentation.** 2024. Disponível em: <https://docs.docker.com/>. Acesso em: mar. 2026.

3. ELMASRI, R.; NAVATHE, S. B. **Sistemas de banco de dados.** 6. ed. São Paulo: Pearson Addison Wesley, 2011.

4. FIELDING, R. T. **Architectural Styles and the Design of Network-based Software Architectures.** 2000. Dissertação (Doutorado em Ciência da Computação) — University of California, Irvine, 2000.

5. HUMBLE, J.; FARLEY, D. **Continuous Delivery:** Reliable Software Releases through Build, Test, and Deployment Automation. Upper Saddle River: Addison-Wesley, 2010.

6. LÜCK, H. **Dimensões da gestão escolar e suas competências.** Curitiba: Positivo, 2009.

7. MARTIN, R. C. **Clean Code:** A Handbook of Agile Software Craftsmanship. Upper Saddle River: Prentice Hall, 2009.

8. MELL, P.; GRANCE, T. **The NIST Definition of Cloud Computing.** Gaithersburg: National Institute of Standards and Technology, 2011. (Special Publication 800-145).

9. MORAN, J. M. Mudando a educação com metodologias ativas. In: SOUZA, C. A. de; MORALES, O. E. T. (Org.). **Convergências midiáticas, educação e cidadania:** aproximações jovens. Ponta Grossa: UEPG, 2015. p. 15-33.

10. PRESSMAN, R. S.; MAXIM, B. R. **Engenharia de Software:** uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.

11. SOMMERVILLE, I. **Engenharia de Software.** 9. ed. São Paulo: Pearson Prentice Hall, 2011.

12. W3C — WORLD WIDE WEB CONSORTIUM. **Web Content Accessibility Guidelines (WCAG) 2.1.** 2018. Disponível em: <https://www.w3.org/TR/WCAG21/>. Acesso em: mar. 2026.

- [ ] **Step 2: Remover nota de rodapé sobre diretrizes USP**

Remover o bloco final sobre "Diretrizes para confecção de teses da USP" que é do template.

---

## Task 10: Listas de ilustrações e tabelas (`listas.tex`)

**Files:**
- Modify: `docs/partial-report/content/listas.tex`

- [ ] **Step 1: Atualizar listas com figuras e tabelas reais**

Atualizar conforme as figuras inseridas na Task 8. As entradas de BRAINSTORM e PROBLEMAS IDENTIFICADOS do template devem ser substituídas pelas figuras reais (dashboard, diagrama, screenshots).

> Nota: os números de página serão atualizados após compilação final.

---

## Task 11: Anexos e Apêndices

**Files:**
- Modify: `docs/partial-report/content/anexos.tex`
- Modify: `docs/partial-report/content/apendices.tex`

- [ ] **Step 1: Adicionar anexos**

Anexo A — Termo de Autorização da Empresa/Instituição (referência ao documento em `docs/company-authorization-term/`)

- [ ] **Step 2: Adicionar apêndices**

Apêndice A — Termo de Consentimento Livre e Esclarecido (TCLE) (referência ao documento em `docs/consent-term/`)
Apêndice B — Plano de Ação (referência ao PDF entregue)

---

## Task 12: Revisão final e compilação

**Files:**
- Modify: `docs/partial-report/main.tex` (atualizar `\docpaginas`)
- Modify: `docs/partial-report/content/listas.tex` (números de página finais)

- [ ] **Step 1: Compilar o documento completo**

```bash
cd docs && make partial-report
```

- [ ] **Step 2: Verificar no PDF**

Checklist:
- [ ] Capa com dados corretos
- [ ] Folha de rosto com dados corretos
- [ ] Ficha catalográfica com nomes ABNT
- [ ] Resumo legível e dentro de 250 palavras
- [ ] Sumário gerado automaticamente com páginas corretas
- [ ] Introdução com citações
- [ ] Desenvolvimento completo (5 subseções)
- [ ] Figuras renderizadas (ou placeholders claros)
- [ ] Referências em ordem alfabética
- [ ] Paginação arábica a partir da introdução

- [ ] **Step 3: Atualizar `\docpaginas` com o total real**

- [ ] **Step 4: Recompilar e gerar PDF final**
