/**
 * server/index.mjs — Express API for career-ops dashboard
 *
 * Routes:
 *   GET  /api/applications        → JSON array of all applications
 *   GET  /api/applications/metrics → pipeline aggregate stats
 *   PATCH /api/applications/:id   → update status in applications.md
 *   GET  /api/report/:id          → report metadata + raw markdown
 *
 * CAREER_OPS_PATH env var sets the root directory (defaults to parent folder).
 */

import express from 'express';
import { dirname, join, resolve } from 'path';
import { fileURLToPath } from 'url';
import { applicationsRouter } from './routes/applications.mjs';
import { reportsRouter } from './routes/reports.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(process.env.CAREER_OPS_PATH ?? join(__dirname, '..'));
const PORT = process.env.API_PORT ?? 3001;

const app = express();
app.use(express.json());

// CORS for Vite dev server
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:5173');
  res.setHeader('Access-Control-Allow-Methods', 'GET, PATCH, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.sendStatus(204);
  next();
});

app.use('/api/applications', applicationsRouter(ROOT));
app.use('/api/report', reportsRouter(ROOT));

app.get('/api/health', (req, res) => res.json({ ok: true, root: ROOT }));

app.listen(PORT, () => {
  console.log(`career-ops API → http://localhost:${PORT}`);
  console.log(`  data root    : ${ROOT}`);
});
