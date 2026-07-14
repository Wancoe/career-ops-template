<script>
  import { fetchApplications, fetchMetrics } from './lib/api.js';
  import Sidebar from './lib/Sidebar.svelte';
  import MetricsBar from './lib/MetricsBar.svelte';
  import SearchBox from './lib/SearchBox.svelte';
  import PipelineTable from './lib/PipelineTable.svelte';
  import PreviewPanel from './lib/PreviewPanel.svelte';

  let applications = $state([]);
  let metrics      = $state(null);
  let loading      = $state(true);
  let error        = $state('');

  // Filter / search / sort state
  let selectedApp  = $state(null);
  let activeFilter = $state('all');
  let searchText   = $state('');
  let sortMode     = $state('score');

  // $derived auto-recomputes whenever applications, activeFilter, searchText, or sortMode change
  const filteredApps = $derived(() => {
    let list = applications;

    // 1. Status filter
    if (activeFilter !== 'all') {
      list = list.filter(a => a.statusNorm === activeFilter);
    }

    // 2. Text search (company + role + notes)
    const q = searchText.trim().toLowerCase();
    if (q) {
      list = list.filter(a =>
        a.company.toLowerCase().includes(q) ||
        a.role.toLowerCase().includes(q) ||
        a.notes.toLowerCase().includes(q)
      );
    }

    // 3. Sort
    list = [...list].sort((a, b) => {
      if (sortMode === 'score')   return b.score - a.score;
      if (sortMode === 'date')    return b.date.localeCompare(a.date);
      if (sortMode === 'company') return a.company.localeCompare(b.company);
      if (sortMode === 'status')  return a.statusNorm.localeCompare(b.statusNorm);
      return 0;
    });

    return list;
  });

  $effect(() => { load(); });

  async function load() {
    loading = true;
    error = '';
    try {
      [applications, metrics] = await Promise.all([fetchApplications(), fetchMetrics()]);
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }
</script>

<div class="app-shell">
  <header class="nav">
    <span class="nav-logo">⚡ Career-Ops</span>
    <span class="nav-sub">Pipeline Dashboard</span>
    {#if loading}<span class="nav-status">Loading…</span>{/if}
    {#if error}<span class="nav-error">{error}</span>{/if}
  </header>

  <div class="body">
    <Sidebar {applications} {activeFilter} onFilter={(k) => activeFilter = k} />

    <main class="main" class:has-panel={!!selectedApp}>
      <MetricsBar {metrics} />

      <SearchBox value={searchText} onSearch={(v) => searchText = v} />

      <PipelineTable
        apps={filteredApps()}
        {sortMode}
        onSelect={(app) => selectedApp = app}
        onSort={(col) => sortMode = col}
      />
    </main>

    <PreviewPanel app={selectedApp} onClose={() => selectedApp = null} onRefresh={load} />
  </div>
</div>

<style>
  .app-shell {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background: var(--bg-canvas);
  }

  .nav {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 20px;
    height: 48px;
    background: var(--bg-default);
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
  }

  .nav-logo   { font-weight: 600; font-size: 15px; color: var(--text-primary); }
  .nav-sub    { font-size: 13px; color: var(--text-muted); }
  .nav-status { font-size: 12px; color: var(--text-muted); margin-left: auto; }
  .nav-error  { font-size: 12px; color: var(--accent-red); margin-left: auto; }

  .body { display: flex; flex: 1; overflow: hidden; }

  .main {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    padding: 16px;
    gap: 12px;
  }
</style>
