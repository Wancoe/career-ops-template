const BASE = '/api';

export async function fetchApplications() {
  const res = await fetch(`${BASE}/applications`);
  if (!res.ok) throw new Error(`fetchApplications: ${res.status}`);
  return res.json();
}

export async function fetchMetrics() {
  const res = await fetch(`${BASE}/applications/metrics`);
  if (!res.ok) throw new Error(`fetchMetrics: ${res.status}`);
  return res.json();
}

export async function fetchReport(id) {
  const res = await fetch(`${BASE}/report/${id}`);
  if (!res.ok) throw new Error(`fetchReport: ${res.status}`);
  return res.json();
}

export async function updateStatus(reportNumber, oldStatus, newStatus) {
  const res = await fetch(`${BASE}/applications/${reportNumber}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ oldStatus, newStatus }),
  });
  if (!res.ok) throw new Error(`updateStatus: ${res.status}`);
  return res.json();
}
