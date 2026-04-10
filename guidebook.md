# Career-Ops Guidebook

## Introduction

Welcome to your personal guidebook for the Career-Ops project! This document is designed specifically for you as you're learning about software development, VS Code, terminal usage, scripting, and AI-assisted coding with Copilot. Career-Ops is an open-source AI-powered job search toolkit that helps evaluate offers, tailor applications, and manage your pipeline.

This guide will break down the project's stack, how it was built from scratch, and provide learning resources to help you understand and potentially extend it. You can convert this Markdown file to PDF using tools like Pandoc or VS Code extensions for easy reference.

## Project Overview

Career-Ops is a local, AI-assisted job search automation tool. It doesn't require external servers—just your machine, some scripts, and an AI assistant. Key features include:

- **Offer Evaluation**: Structured A-F scoring of job offers across 10 dimensions
- **CV Generation**: ATS-optimized resumes tailored per job
- **Portal Scanning**: Automated discovery of new opportunities
- **Batch Processing**: Parallel evaluation of multiple offers
- **Pipeline Tracking**: Markdown-based tracker with integrity checks
- **Dashboard**: Optional TUI (Terminal User Interface) for browsing

The project emphasizes quality over quantity—helping you find the right fits rather than spamming applications.

## Tech Stack

### Programming Languages

- **Primary**: Node.js (JavaScript/TypeScript)
  - Used for all core scripts, utilities, and automation
  - Handles PDF generation, scanning, and data processing
- **Secondary**: Go
  - Used for the optional TUI dashboard
  - Provides a fast, cross-platform terminal interface

### Frameworks and Libraries

- **Playwright**: Browser automation for PDF generation and job scanning
  - Handles headless Chrome operations for reliable web interactions
- **Bubble Tea + Lipgloss**: Go libraries for the TUI dashboard
  - Bubble Tea: Framework for building terminal apps
  - Lipgloss: Styling and layout for terminal UIs
- **Node.js Ecosystem**:
  - `fs/promises`: Async file operations
  - `path`: Path manipulation
  - Custom modules for career evaluation logic

### Tools and Infrastructure

- **Version Control**: Git
- **Package Management**: npm (Node.js), Go modules
- **Configuration**: YAML for settings, Markdown for data
- **AI Integration**: Designed to work with AI assistants like Copilot
- **Testing**: Custom test scripts (`test-all.mjs`)
- **Documentation**: Markdown files throughout

### Architecture Patterns

- **Local-First**: Everything runs on your machine
- **Script-Based**: No complex build systems—just Node.js scripts
- **Modular**: Separate modes for different operations
- **Data-Driven**: YAML configs, Markdown data files

## How to Build from Scratch

### Step 1: Project Setup

1. Create a new directory: `mkdir career-ops && cd career-ops`
2. Initialize Git: `git init`
3. Create `package.json`:

```json
{
  "name": "career-ops",
  "version": "1.0.0",
  "description": "AI-powered job search toolkit",
  "main": "index.js",
  "scripts": {
    "test": "node test-all.mjs"
  },
  "dependencies": {
    "playwright": "^1.40.0"
  }
}
```

4. Install dependencies: `npm install`

### Step 2: Core Structure

Create these directories and files:

```
career-ops/
├── data/           # Markdown data files
├── modes/          # AI assistant modes
├── templates/      # HTML/CSS templates
├── scripts/        # Utility scripts
├── batch/          # Batch processing
├── dashboard/      # Go TUI (optional)
├── docs/           # Documentation
└── config/         # YAML configurations
```

### Step 3: Basic Scripts

Start with simple Node.js scripts:

- `doctor.mjs`: Health check script
- `generate-pdf.mjs`: HTML to PDF conversion
- `scan.mjs`: Basic job scanning

### Step 4: AI Integration

Create mode files in `modes/` that define how the AI assistant should behave:

- `_shared.md`: Common evaluation logic
- `oferta.md`: Job offer evaluation mode
- `pdf.md`: CV generation mode

### Step 5: Data Management

Use Markdown tables for tracking:

```markdown
# Applications Tracker

| # | Date | Company | Role | Score | Status | PDF | Report | Notes |
|---|------|---------|------|-------|--------|-----|--------|-------|
```

### Step 6: Testing and Iteration

- Write comprehensive tests in `test-all.mjs`
- Test each component individually
- Iterate based on real usage

## Programming Language Deep Dive: Node.js

Since Career-Ops is primarily built with Node.js, here's what you need to know:

### Why Node.js?

- **JavaScript Everywhere**: Runs on servers, browsers, and desktops
- **Async/Await**: Modern asynchronous programming
- **Rich Ecosystem**: Thousands of libraries via npm
- **Cross-Platform**: Works on Windows, macOS, Linux

### Key Concepts in Career-Ops

1. **Modules**: Use ES modules (`import/export`)
2. **File System**: `fs/promises` for async file operations
3. **Command Line**: `process.argv` for script arguments
4. **Error Handling**: Try/catch with async functions

### Learning Resources

- **Official Docs**: nodejs.org
- **MDN JavaScript**: developer.mozilla.org
- **Node.js Best Practices**: github.com/goldbergyoni/nodebestpractices
- **FreeCodeCamp**: freecodecamp.org/learn/javascript-algorithms-and-data-structures/

### Example from Career-Ops

```javascript
import { readFile, writeFile } from 'fs/promises';
import { chromium } from 'playwright';

async function generatePDF(htmlPath, pdfPath) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const html = await readFile(htmlPath, 'utf8');
  await page.setContent(html);
  await page.pdf({ path: pdfPath, format: 'A4' });
  await browser.close();
}
```

## Learning Resources

### VS Code

VS Code is your primary development environment. Key features:

- **Extensions**: Install Copilot, Prettier, ESLint
- **Integrated Terminal**: Run commands without leaving the editor
- **Debugging**: Built-in debugger for Node.js
- **Git Integration**: Stage, commit, push directly

**Tips**:
- Use Ctrl+Shift+P for command palette
- Ctrl+` to toggle terminal
- F5 to start debugging
- Learn keyboard shortcuts gradually

### Terminal Usage

The terminal is essential for running scripts and Git commands.

**Basic Commands**:
- `cd`: Change directory
- `ls`/`dir`: List files
- `mkdir`: Create directory
- `git status`: Check repository status
- `node script.mjs`: Run Node.js script

**PowerShell (Windows)**:
- Use `;` to chain commands
- `Get-ChildItem` instead of `ls`
- `Set-Location` instead of `cd`

**Learning**: Practice daily. Start with file operations, then Git, then npm.

### Scripts and Automation

Career-Ops uses `.mjs` files for scripts. Key concepts:

- **Shebang**: `#!/usr/bin/env node` for executable scripts
- **Arguments**: `process.argv.slice(2)` for command-line args
- **Async Functions**: Use `async/await` for file operations
- **Error Handling**: Always wrap in try/catch

### Copilot Usage and Better Prompts

Copilot is your AI coding assistant. Here's how to use it effectively:

#### How Copilot Works

- **Context-Aware**: Reads your open files and recent edits
- **Pattern Recognition**: Learns from millions of code examples
- **Inline Suggestions**: Provides completions as you type
- **Chat Interface**: Ask questions and get explanations

#### Writing Better Prompts

**For Code Generation**:
- Be specific: "Write a Node.js function to read a YAML file and parse it"
- Include context: "In the context of a job search app..."
- Specify format: "Return the result as an async function"

**For Code Improvement**:
- "Refactor this function to use async/await"
- "Add error handling to this script"
- "Optimize this for performance"

**For Learning**:
- "Explain how this Node.js code works"
- "What does this regex pattern match?"
- "Show me an example of using Playwright"

#### Best Practices

1. **Start Small**: Let Copilot complete simple statements first
2. **Provide Context**: Open relevant files, comment your intent
3. **Iterate**: Accept suggestions, then refine
4. **Learn Patterns**: Study Copilot's suggestions to understand best practices
5. **Use Comments**: Write descriptive comments to guide Copilot

#### Common Prompt Patterns

- **Function Creation**: "Create a function that [does X] using [library]"
- **Error Handling**: "Add try/catch to this async function"
- **Documentation**: "Add JSDoc comments to this function"
- **Testing**: "Write a test for this function"
- **Refactoring**: "Simplify this code" or "Make this more readable"

#### When Copilot Struggles

- Complex multi-step logic: Break into smaller functions
- Domain-specific knowledge: Provide more context
- Novel solutions: Guide with examples or requirements

## Conclusion

Career-Ops demonstrates how to build a practical tool using modern web technologies and AI assistance. By studying this project, you'll learn:

- Full-stack development with Node.js and Go
- Browser automation with Playwright
- Data management with Markdown and YAML
- AI-assisted development workflows
- Terminal and Git best practices

Remember: Start small, experiment often, and use Copilot as a learning tool rather than just a code generator. The goal is understanding, not just completion.

Happy coding! 🚀