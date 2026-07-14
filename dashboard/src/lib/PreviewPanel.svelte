<script>
  import ReportViewer from './ReportViewer.svelte';
  import StatusDropdown from './StatusDropdown.svelte';
  import { fetchReport } from './api.js';

  let { app = null, onClose = () => {}, onRefresh = () => {} } = $props();

  let reportData  = $state(null);
  let showReport  = $state(false);
  let loadingMeta = $state(false);

  // Fetch report metadata when a new app is selected
  $effect(() => {
    reportData = null;
    showReport = false;
    if (!app?.reportNumber) return;
    loadingMeta = true;
    fetchReport(app.reportNumber)
      .then(d => { reportData = d; })
      .catch(() => {})
      .finally(() => { loadingMeta = false; });
  });

  function scoreColor(score) {
    if (score >= 4.5) return '#3fb950';
    if (score >= 3.5) return '#d29922';
    return '#f85149';
  }
</script>

{#if showReport && app?.reportNumber}
  <ReportViewer reportNumber={app.reportNumber} onClose={() => showReport = false} />
{/if}

{#if app}
  <aside class="panel">
    <div class="panel-header">
      <div class="panel-company">{app.company}</div>
      <button class="close-btn" onclick={onClose}>✕</button>
    </div>

    <div class="panel-body">
      <div class="panel-role">{app.role}</div>
      <div class="panel-date">{app.date}</div>

      <!-- Score -->
      <div class="score-section">
        <span class="score-num" style="color:{scoreColor(app.score)}">{app.score > 0 ? app.score + '/5' : '—'}</span>
        {#if app.score > 0}
          <div class="score-bar-bg">
            <div class="score-bar-fill" style="width:{(app.score/5)*100}%; background:{scoreColor(app.score)}"></div>
          </div>
        {/if}
      </div>

      <!-- Metadata from report -->
      {#if loadingMeta}
        <div class="meta-loading">Loading report data…</div>
      {:else if reportData}
        {#if reportData.archetype}
          <div class="meta-row"><span class="meta-label">Archetype</span><span class="meta-val">{reportData.archetype}</span></div>
        {/if}
        {#if reportData.remote}
          <div class="meta-row"><span class="meta-label">Remote</span><span class="meta-val">{reportData.remote}</span></div>
        {/if}
        {#if reportData.comp}
          <div class="meta-row"><span class="meta-label">Comp</span><span class="meta-val">{reportData.comp}</span></div>
        {/if}
        {#if reportData.tldr}
          <div class="meta-tldr">{reportData.tldr}</div>
        {/if}
      {/if}

      <!-- Notes -->
      {#if app.notes}
        <div class="meta-notes">{app.notes}</div>
      {/if}

      <!-- Status editor -->
      <StatusDropdown {app} onSaved={() => onRefresh()} />

      <!-- Action buttons -->
      <div class="actions">
        {#if app.jobURL}
          <a class="btn btn-primary" href={app.jobURL} target="_blank" rel="noopener">Open Job</a>
        {/if}
        {#if app.reportNumber}
          <button class="btn btn-secondary" onclick={() => showReport = true}>View Report</button>
        {/if}
      </div>
    </div>
  </aside>
{/if}

<style>
  .panel {
    width: 300px;
    flex-shrink: 0;
    background: var(--bg-default);
    border-left: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .panel-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
  }

  .panel-company { font-weight: 600; font-size: 14px; }

  .close-btn {
    background: none;
    border: none;
    color: var(--text-muted);
    cursor: pointer;
    font-size: 14px;
    padding: 2px 4px;
    border-radius: 4px;
  }

  .close-btn:hover { color: var(--text-primary); background: var(--bg-subtle); }

  .panel-body {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .panel-role { font-size: 13px; color: var(--text-primary); }
  .panel-date { font-size: 12px; color: var(--text-muted); }

  .score-section { display: flex; align-items: center; gap: 10px; }
  .score-num { font-size: 24px; font-weight: 700; }
  .score-bar-bg { flex: 1; height: 6px; background: var(--bg-subtle); border-radius: 3px; overflow: hidden; }
  .score-bar-fill { height: 100%; border-radius: 3px; transition: width 0.3s; }

  .meta-row { display: flex; gap: 8px; font-size: 12px; }
  .meta-label { color: var(--text-muted); min-width: 64px; flex-shrink: 0; }
  .meta-val { color: var(--text-primary); }

  .meta-tldr {
    font-size: 12px;
    color: var(--text-muted);
    line-height: 1.5;
    padding: 8px 10px;
    background: var(--bg-subtle);
    border-radius: 6px;
    border-left: 2px solid var(--accent-blue);
  }

  .meta-notes {
    font-size: 12px;
    color: var(--text-muted);
    line-height: 1.5;
  }

  .meta-loading { font-size: 12px; color: var(--text-muted); }

  .actions { display: flex; flex-direction: column; gap: 8px; margin-top: auto; padding-top: 16px; }

  .btn {
    display: block;
    text-align: center;
    padding: 7px 12px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
    border: 1px solid transparent;
    transition: opacity 0.1s;
  }

  .btn:hover { opacity: 0.85; }

  .btn-primary { background: var(--accent-blue); color: #fff; }
  .btn-secondary { background: var(--bg-subtle); border-color: var(--border); color: var(--text-primary); }
</style>
