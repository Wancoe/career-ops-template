<script>
  let { applications = [], activeFilter = 'all', onFilter = () => {} } = $props();

  const STATUS_KEYS = ['evaluated', 'applied', 'interview', 'offer', 'responded', 'rejected', 'discarded', 'skip'];

  const counts = $derived(() => {
    const c = { all: applications.length };
    for (const k of STATUS_KEYS) c[k] = 0;
    for (const a of applications) {
      const s = a.statusNorm;
      if (c[s] !== undefined) c[s]++;
    }
    return c;
  });

  const statuses = [
    { key: 'all',       label: 'All'       },
    { key: 'evaluated', label: 'Evaluated' },
    { key: 'applied',   label: 'Applied'   },
    { key: 'interview', label: 'Interview' },
    { key: 'offer',     label: 'Offer'     },
    { key: 'responded', label: 'Responded' },
    { key: 'rejected',  label: 'Rejected'  },
    { key: 'discarded', label: 'Discarded' },
    { key: 'skip',      label: 'Skip'      },
  ];
</script>

<aside class="sidebar">
  <div class="section-title">Filter</div>
  {#each statuses as s}
    <button
      class="filter-btn"
      class:active={activeFilter === s.key}
      onclick={() => onFilter(s.key)}
    >
      <span class="label">{s.label}</span>
      <span class="count">{counts()[s.key] ?? 0}</span>
    </button>
  {/each}
</aside>

<style>
  .sidebar {
    width: 180px;
    flex-shrink: 0;
    background: var(--bg-default);
    border-right: 1px solid var(--border);
    padding: 12px 8px;
    display: flex;
    flex-direction: column;
    gap: 2px;
    overflow-y: auto;
  }

  .section-title {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted);
    padding: 4px 8px 8px;
  }

  .filter-btn {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6px 10px;
    border-radius: 6px;
    border: none;
    background: transparent;
    color: var(--text-muted);
    cursor: pointer;
    font-size: 13px;
    text-align: left;
    transition: background 0.1s, color 0.1s;
    width: 100%;
  }

  .filter-btn:hover { background: var(--bg-subtle); color: var(--text-primary); }
  .filter-btn.active { background: var(--accent-blue); color: #fff; }

  .count { font-size: 11px; opacity: 0.7; }
</style>
