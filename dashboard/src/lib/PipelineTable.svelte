<script>
  let { apps = [], onSelect = () => {}, onSort = () => {}, sortMode = 'score' } = $props();

  const STATUS_COLORS = {
    interview:  '#3fb950',
    offer:      '#bc8cff',
    responded:  '#58a6ff',
    applied:    '#1f6feb',
    evaluated:  '#d29922',
    rejected:   '#f85149',
    discarded:  '#6e7681',
    skip:       '#6e7681',
  };

  function scoreColor(score) {
    if (score >= 4.5) return '#3fb950';
    if (score >= 3.5) return '#d29922';
    return '#f85149';
  }

  function colLabel(col) {
    return sortMode === col ? '▼ ' : '';
  }
</script>

<div class="table-wrap">
  <table>
    <thead>
      <tr>
        <th class="th-num">#</th>
        <th class="th-date" onclick={() => onSort('date')}>{colLabel('date')}Date</th>
        <th onclick={() => onSort('company')}>{colLabel('company')}Company</th>
        <th>Role</th>
        <th class="th-score" onclick={() => onSort('score')}>{colLabel('score')}Score</th>
        <th class="th-status" onclick={() => onSort('status')}>{colLabel('status')}Status</th>
        <th class="th-notes">Notes</th>
      </tr>
    </thead>
    <tbody>
      {#each apps as app (app.number)}
        <tr onclick={() => onSelect(app)}>
          <td class="td-num">{app.number}</td>
          <td class="td-date">{app.date}</td>
          <td class="td-company">{app.company}</td>
          <td class="td-role">{app.role}</td>
          <td class="td-score">
            {#if app.score > 0}
              <div class="score-wrap">
                <div class="score-bar" style="width:{(app.score/5)*60}px; background:{scoreColor(app.score)}"></div>
                <span style="color:{scoreColor(app.score)}">{app.score}</span>
              </div>
            {:else}
              <span class="muted">—</span>
            {/if}
          </td>
          <td class="td-status">
            <span class="badge" style="color:{STATUS_COLORS[app.statusNorm] ?? '#8b949e'}">
              {app.statusNorm}
            </span>
          </td>
          <td class="td-notes">{app.notes}</td>
        </tr>
      {/each}
      {#if apps.length === 0}
        <tr><td colspan="7" class="empty">No applications found.</td></tr>
      {/if}
    </tbody>
  </table>
</div>

<style>
  .table-wrap {
    flex: 1;
    overflow-y: auto;
    background: var(--bg-default);
    border: 1px solid var(--border);
    border-radius: 8px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }

  thead {
    position: sticky;
    top: 0;
    z-index: 1;
    background: var(--bg-subtle);
  }

  th {
    padding: 8px 12px;
    text-align: left;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    color: var(--text-muted);
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    user-select: none;
    white-space: nowrap;
  }

  th:hover { color: var(--text-primary); }

  td {
    padding: 8px 12px;
    border-bottom: 1px solid var(--border-muted);
    vertical-align: middle;
  }

  tr:last-child td { border-bottom: none; }

  tr:hover td { background: var(--bg-subtle); cursor: pointer; }

  .th-num, .td-num { width: 36px; color: var(--text-muted); }
  .th-date, .td-date { width: 96px; white-space: nowrap; color: var(--text-muted); }
  .th-score, .td-score { width: 110px; }
  .th-status, .td-status { width: 100px; }
  .td-company { font-weight: 500; }
  .td-notes { color: var(--text-muted); font-size: 12px; max-width: 260px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

  .score-wrap { display: flex; align-items: center; gap: 6px; }
  .score-bar { height: 4px; border-radius: 2px; flex-shrink: 0; }

  .badge { font-size: 12px; font-weight: 500; text-transform: capitalize; }

  .muted { color: var(--text-muted); }
  .empty { text-align: center; padding: 32px; color: var(--text-muted); }
</style>
