import { Router } from 'express';
import { readdirSync, existsSync } from 'fs';
import { join } from 'path';
import { loadReportSummary } from '../parser.mjs';

export function reportsRouter(root) {
  const router = Router();

  // GET /api/report/:id  — returns report metadata + raw markdown
  router.get('/:id', (req, res) => {
    const { id } = req.params;
    const reportsDir = join(root, 'reports');
    if (!existsSync(reportsDir)) return res.status(404).json({ error: 'reports/ directory not found' });

    // Find the report file matching the numeric ID prefix
    const files = readdirSync(reportsDir);
    const match = files.find(f => f.startsWith(id.padStart(3, '0') + '-') || f.startsWith(id + '-'));
    if (!match) return res.status(404).json({ error: `Report ${id} not found` });

    const reportPath = `reports/${match}`;
    const summary = loadReportSummary(root, reportPath);
    if (!summary.rawText) return res.status(404).json({ error: 'Could not read report' });

    res.json({
      id,
      file: match,
      archetype: summary.archetype,
      tldr: summary.tldr,
      remote: summary.remote,
      comp: summary.comp,
      rawMarkdown: summary.rawText,
    });
  });

  return router;
}
