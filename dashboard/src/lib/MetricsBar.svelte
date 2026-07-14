<script>
  let { metrics = null } = $props();
</script>

<div class="metrics-bar">
  <div class="metric">
    <span class="metric-value">{metrics?.total ?? '—'}</span>
    <span class="metric-label">Total</span>
  </div>
  <div class="metric">
    <span class="metric-value">{metrics?.avgScore ?? '—'}</span>
    <span class="metric-label">Avg Score</span>
  </div>
  <div class="metric">
    <span class="metric-value">{metrics?.actionable ?? '—'}</span>
    <span class="metric-label">Actionable</span>
  </div>
  <div class="metric">
    <span class="metric-value">{metrics?.byStatus?.interview ?? 0}</span>
    <span class="metric-label">Interviews</span>
  </div>
  <div class="metric">
    <span class="metric-value">{metrics?.byStatus?.applied ?? 0}</span>
    <span class="metric-label">Applied</span>
  </div>
  <div class="metric">
    <span class="metric-value">{metrics?.topScore ?? '—'}</span>
    <span class="metric-label">Top Score</span>
  </div>
</div>

<style>
  .metrics-bar {
    display: flex;
    gap: 0;
    background: var(--bg-default);
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    flex-shrink: 0;
  }

  .metric {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 12px 8px;
    border-right: 1px solid var(--border);
  }

  .metric:last-child {
    border-right: none;
  }

  .metric-value {
    font-size: 22px;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1;
  }

  .metric-label {
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
  }
</style>
