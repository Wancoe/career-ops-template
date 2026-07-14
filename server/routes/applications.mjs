import { Router } from 'express';
import { parseApplications, computeMetrics, updateApplicationStatus } from '../parser.mjs';

export function applicationsRouter(root) {
  const router = Router();

  router.get('/', (req, res) => {
    try {
      const apps = parseApplications(root);
      res.json(apps);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

  router.get('/metrics', (req, res) => {
    try {
      const apps = parseApplications(root);
      res.json(computeMetrics(apps));
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

  router.patch('/:reportNumber', (req, res) => {
    const { reportNumber } = req.params;
    const { oldStatus, newStatus } = req.body;
    if (!newStatus) return res.status(400).json({ error: 'newStatus is required' });
    try {
      updateApplicationStatus(root, reportNumber, oldStatus ?? '', newStatus);
      res.json({ ok: true });
    } catch (err) {
      res.status(404).json({ error: err.message });
    }
  });

  return router;
}
