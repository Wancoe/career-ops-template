/**
 * parser.mjs — JS port of dashboard/internal/data/career.go
 *
 * Parses data/applications.md and report files into plain JS objects.
 * All logic mirrors the Go implementation line-for-line so the two stay in sync.
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join } from 'path';

// ── Regexes (mirrors var block in career.go) ────────────────────
const RE_REPORT_LINK   = /\[(\d+)\]\(([^)]+)\)/;
const RE_SCORE_VALUE   = /(\d+\.?\d*)\/5/;
const RE_ARCHETYPE     = /\*\*Arquetipo(?:\s+detectado)?\*\*\s*\|\s*(.+)/i;
const RE_TLDR          = /\*\*TL;DR\*\*\s*\|\s*(.+)/i;
const RE_TLDR_COLON    = /\*\*TL;DR:\*\*\s*(.+)/i;
const RE_REMOTE        = /\*\*Remote\*\*\s*\|\s*(.+)/i;
const RE_COMP          = /\*\*Comp\*\*\s*\|\s*(.+)/i;
const RE_ARCHETYPE_COL = /\*\*Arquetipo:\*\*\s*(.+)/i;
const RE_REPORT_URL    = /^\*\*URL:\*\*\s*(https?:\/\/\S+)/m;
const RE_BATCH_ID      = /^\*\*Batch ID:\*\*\s*(\d+)/m;

// ── Helpers ─────────────────────────────────────────────────────

function cleanTableCell(s) {
  return s.trim().replace(/\|+$/, '').trim();
}

function normalizeCompany(name) {
  let s = name.toLowerCase().trim();
  const suffixes = [' inc.', ' inc', ' llc', ' ltd', ' corp', ' corporation', ' technologies', ' technology', ' group', ' co.'];
  for (const suf of suffixes) {
    if (s.endsWith(suf)) s = s.slice(0, -suf.length);
  }
  return s.trim();
}

// ── normalizeStatus ─────────────────────────────────────────────
// Mirrors NormalizeStatus in career.go — keep aliases in sync with templates/states.yml
export function normalizeStatus(raw) {
  let s = raw.replace(/\*\*/g, '').trim().toLowerCase();
  // Strip trailing date (e.g. "applied 2026-03-12")
  const dateIdx = s.indexOf(' 202');
  if (dateIdx > 0) s = s.slice(0, dateIdx).trim();

  if (s.includes('no aplicar') || s.includes('no_aplicar') || s === 'skip' || s.includes('geo blocker')) return 'skip';
  if (s.includes('interview') || s.includes('entrevista')) return 'interview';
  if (s === 'offer' || s.includes('oferta')) return 'offer';
  if (s.includes('responded') || s.includes('respondido')) return 'responded';
  if (s.includes('applied') || s.includes('aplicado') || s === 'enviada' || s === 'aplicada' || s === 'sent') return 'applied';
  if (s.includes('rejected') || s.includes('rechazado') || s === 'rechazada') return 'rejected';
  if (s.includes('discarded') || s.includes('descartado') || s === 'descartada' || s === 'cerrada' || s === 'cancelada' || s.startsWith('duplicado') || s.startsWith('dup')) return 'discarded';
  if (s.includes('evaluated') || s.includes('evaluada') || s.includes('avaliada') || s === 'condicional' || s === 'hold' || s === 'monitor' || s === 'evaluar' || s === 'verificar') return 'evaluated';
  return s;
}

export function statusPriority(status) {
  const map = { interview: 0, offer: 1, responded: 2, applied: 3, evaluated: 4, skip: 5, rejected: 6, discarded: 7 };
  return map[normalizeStatus(status)] ?? 8;
}

// ── loadBatchInputURLs ───────────────────────────────────────────
function loadBatchInputURLs(root) {
  const p = join(root, 'batch', 'batch-input.tsv');
  if (!existsSync(p)) return {};
  const result = {};
  for (const line of readFileSync(p, 'utf-8').split('\n')) {
    const fields = line.split('\t');
    if (fields.length < 4 || fields[0] === 'id') continue;
    const id = fields[0];
    const notes = fields[3];
    const pipeIdx = notes.lastIndexOf('| ');
    if (pipeIdx >= 0) {
      const u = notes.slice(pipeIdx + 2).trim();
      if (u.startsWith('http')) { result[id] = u; continue; }
    }
    if (fields[1].startsWith('http')) result[id] = fields[1];
  }
  return result;
}

// ── loadJobURLs ──────────────────────────────────────────────────
function loadJobURLs(root) {
  const inputPath = join(root, 'batch', 'batch-input.tsv');
  const statePath = join(root, 'batch', 'batch-state.tsv');
  if (!existsSync(inputPath) || !existsSync(statePath)) return {};

  const entries = {};
  for (const line of readFileSync(inputPath, 'utf-8').split('\n')) {
    const fields = line.split('\t');
    if (fields.length < 4 || fields[0] === 'id') continue;
    const e = { id: fields[0], url: '', company: '', role: '' };
    const notes = fields[3];
    const pipeIdx = notes.lastIndexOf('| ');
    if (pipeIdx >= 0) {
      const u = notes.slice(pipeIdx + 2).trim();
      if (u.startsWith('http')) e.url = u;
    }
    if (!e.url && fields[1].startsWith('http')) e.url = fields[1];

    let notesPart = notes;
    const firstPipe = notesPart.indexOf(' | ');
    if (firstPipe >= 0) notesPart = notesPart.slice(0, firstPipe);
    const atIdx = notesPart.lastIndexOf(' @ ');
    if (atIdx >= 0) {
      e.role = notesPart.slice(0, atIdx).trim();
      e.company = notesPart.slice(atIdx + 3).trim();
    }
    if (e.url) entries[fields[0]] = e;
  }

  const reportToURL = {};
  for (const line of readFileSync(statePath, 'utf-8').split('\n')) {
    const fields = line.split('\t');
    if (fields.length < 6 || fields[0] === 'id') continue;
    const [id, , status, , , reportNum] = fields;
    if (status !== 'completed' || !reportNum || reportNum === '-') continue;
    const e = entries[id];
    if (e) {
      reportToURL[reportNum] = e.url;
      if (reportNum.length < 3) reportToURL[reportNum.padStart(3, '0')] = e.url;
    }
  }
  return reportToURL;
}

// ── enrichFromScanHistory ────────────────────────────────────────
function enrichFromScanHistory(root, apps) {
  const p = join(root, 'scan-history.tsv');
  if (!existsSync(p)) return;

  const byCompany = {};
  for (const line of readFileSync(p, 'utf-8').split('\n')) {
    const fields = line.split('\t');
    if (fields.length < 5 || fields[0] === 'url') continue;
    const [url, , , title, company] = fields;
    if (!url || !url.startsWith('http')) continue;
    const key = normalizeCompany(company);
    (byCompany[key] ??= []).push({ url, title });
  }

  for (const app of apps) {
    if (app.jobURL) continue;
    const key = normalizeCompany(app.company);
    const matches = byCompany[key] ?? [];
    if (matches.length === 1) {
      app.jobURL = matches[0].url;
    } else if (matches.length > 1) {
      const appRole = app.role.toLowerCase();
      let best = matches[0].url, bestScore = 0;
      for (const m of matches) {
        const score = appRole.split(/\s+/).filter(w => w.length > 2 && m.title.toLowerCase().includes(w)).length;
        if (score > bestScore) { bestScore = score; best = m.url; }
      }
      app.jobURL = best;
    }
  }
}

// ── enrichAppURLsByCompany ───────────────────────────────────────
function enrichAppURLsByCompany(root, apps) {
  const p = join(root, 'batch', 'batch-input.tsv');
  if (!existsSync(p)) return;

  const byCompany = {};
  for (const line of readFileSync(p, 'utf-8').split('\n')) {
    const fields = line.split('\t');
    if (fields.length < 4 || fields[0] === 'id') continue;
    const notes = fields[3];
    let url = '';
    const pipeIdx = notes.lastIndexOf('| ');
    if (pipeIdx >= 0) { const u = notes.slice(pipeIdx + 2).trim(); if (u.startsWith('http')) url = u; }
    if (!url && fields[1].startsWith('http')) url = fields[1];
    if (!url) continue;

    let notesPart = notes;
    const firstPipe = notesPart.indexOf(' | ');
    if (firstPipe >= 0) notesPart = notesPart.slice(0, firstPipe);
    const atIdx = notesPart.lastIndexOf(' @ ');
    if (atIdx >= 0) {
      const role = notesPart.slice(0, atIdx).trim();
      const company = notesPart.slice(atIdx + 3).trim();
      const key = normalizeCompany(company);
      (byCompany[key] ??= []).push({ role, url });
    }
  }

  for (const app of apps) {
    if (app.jobURL) continue;
    const key = normalizeCompany(app.company);
    const matches = byCompany[key] ?? [];
    if (matches.length === 1) {
      app.jobURL = matches[0].url;
    } else if (matches.length > 1) {
      const appRole = app.role.toLowerCase();
      let best = matches[0].url, bestScore = 0;
      for (const m of matches) {
        const score = appRole.split(/\s+/).filter(w => w.length > 2 && m.role.toLowerCase().includes(w)).length;
        if (score > bestScore) { bestScore = score; best = m.url; }
      }
      app.jobURL = best;
    }
  }
}

// ── parseApplications ────────────────────────────────────────────
export function parseApplications(root) {
  let filePath = join(root, 'applications.md');
  if (!existsSync(filePath)) filePath = join(root, 'data', 'applications.md');
  if (!existsSync(filePath)) return [];

  const lines = readFileSync(filePath, 'utf-8').split('\n');
  const apps = [];

  for (const raw of lines) {
    const line = raw.trim();
    if (!line || line.startsWith('# ') || line.startsWith('|---') || line.startsWith('| #')) continue;
    if (!line.startsWith('|')) continue;

    let fields;
    if (line.includes('\t')) {
      const stripped = line.replace(/^\|/, '').trim();
      fields = stripped.split('\t').map(f => f.replace(/^\||\|$/g, '').trim());
    } else {
      fields = line.replace(/^\||\|$/g, '').split('|').map(f => f.trim());
    }

    if (fields.length < 8) continue;

    const app = {
      number: apps.length + 1,
      date: fields[1],
      company: fields[2],
      role: fields[3],
      scoreRaw: fields[4],
      score: 0,
      status: fields[5],
      statusNorm: '',
      hasPDF: fields[6].includes('✅'),
      reportNumber: '',
      reportPath: '',
      notes: fields[8] ?? '',
      jobURL: '',
      archetype: '',
      tldr: '',
      remote: '',
      comp: '',
    };

    const scoreMatch = RE_SCORE_VALUE.exec(fields[4]);
    if (scoreMatch) app.score = parseFloat(scoreMatch[1]);

    const reportMatch = RE_REPORT_LINK.exec(fields[7]);
    if (reportMatch) { app.reportNumber = reportMatch[1]; app.reportPath = reportMatch[2]; }

    app.statusNorm = normalizeStatus(app.status);
    apps.push(app);
  }

  // Enrich with job URLs (5-tier strategy matching Go logic)
  const batchURLs = loadBatchInputURLs(root);
  const reportNumURLs = loadJobURLs(root);

  for (const app of apps) {
    if (!app.reportPath) continue;
    const fullReport = join(root, app.reportPath);
    if (!existsSync(fullReport)) continue;
    let header = readFileSync(fullReport, 'utf-8');
    if (header.length > 1000) header = header.slice(0, 1000);

    const urlMatch = RE_REPORT_URL.exec(header);
    if (urlMatch) { app.jobURL = urlMatch[1]; continue; }

    const batchMatch = RE_BATCH_ID.exec(header);
    if (batchMatch && batchURLs[batchMatch[1]]) { app.jobURL = batchURLs[batchMatch[1]]; continue; }

    if (reportNumURLs[app.reportNumber]) { app.jobURL = reportNumURLs[app.reportNumber]; continue; }
  }

  enrichFromScanHistory(root, apps);
  enrichAppURLsByCompany(root, apps);

  return apps;
}

// ── loadReportSummary ────────────────────────────────────────────
export function loadReportSummary(root, reportPath) {
  const fullPath = join(root, reportPath);
  if (!existsSync(fullPath)) return {};
  const text = readFileSync(fullPath, 'utf-8');

  let archetype = '';
  const archMatch = RE_ARCHETYPE.exec(text) ?? RE_ARCHETYPE_COL.exec(text);
  if (archMatch) archetype = cleanTableCell(archMatch[1]);

  let tldr = '';
  const tldrMatch = RE_TLDR.exec(text) ?? RE_TLDR_COLON.exec(text);
  if (tldrMatch) tldr = cleanTableCell(tldrMatch[1]);
  if (tldr.length > 120) tldr = tldr.slice(0, 117) + '...';

  let remote = '';
  const remoteMatch = RE_REMOTE.exec(text);
  if (remoteMatch) remote = cleanTableCell(remoteMatch[1]);

  let comp = '';
  const compMatch = RE_COMP.exec(text);
  if (compMatch) comp = cleanTableCell(compMatch[1]);

  return { archetype, tldr, remote, comp, rawText: text };
}

// ── computeMetrics ───────────────────────────────────────────────
export function computeMetrics(apps) {
  const byStatus = {};
  let totalScore = 0, scored = 0, topScore = 0, withPDF = 0, actionable = 0;

  for (const app of apps) {
    const s = app.statusNorm;
    byStatus[s] = (byStatus[s] ?? 0) + 1;
    if (app.score > 0) {
      totalScore += app.score;
      scored++;
      if (app.score > topScore) topScore = app.score;
    }
    if (app.hasPDF) withPDF++;
    if (s !== 'skip' && s !== 'rejected' && s !== 'discarded') actionable++;
  }

  return {
    total: apps.length,
    byStatus,
    avgScore: scored > 0 ? Math.round((totalScore / scored) * 10) / 10 : 0,
    topScore,
    withPDF,
    actionable,
  };
}

// ── updateApplicationStatus ──────────────────────────────────────
export function updateApplicationStatus(root, reportNumber, oldStatus, newStatus) {  // sync
  let filePath = join(root, 'applications.md');
  if (!existsSync(filePath)) filePath = join(root, 'data', 'applications.md');
  if (!existsSync(filePath)) throw new Error('applications.md not found');

  const content = readFileSync(filePath, 'utf-8');
  const lines = content.split('\n');
  let found = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line.trim().startsWith('|')) continue;
    if (reportNumber && line.includes(`[${reportNumber}]`)) {
      lines[i] = line.replace(oldStatus, newStatus);
      found = true;
      break;
    }
  }

  if (!found) throw new Error(`Application not found: report ${reportNumber}`);

  writeFileSync(filePath, lines.join('\n'), 'utf-8');
}
