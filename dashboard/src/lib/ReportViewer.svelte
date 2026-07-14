<script>
  import { fetchReport } from './api.js';
  import { marked } from 'marked';

  let { reportNumber = '', onClose = () => {} } = $props();

  let html    = $state('');
  let loading = $state(true);
  let error   = $state('');

  $effect(() => {
    if (!reportNumber) return;
    loading = true;
    error = '';
    fetchReport(reportNumber)
      .then(d => { html = marked.parse(d.rawMarkdown ?? ''); })
      .catch(e => { error = e.message; })
      .finally(() => { loading = false; });
  });
</script>

<div class="viewer">
  <div class="viewer-header">
    <span class="viewer-title">Report #{reportNumber}</span>
    <button class="close-btn" onclick={onClose}>✕ Close</button>
  </div>

  {#if loading}
    <div class="state">Loading report…</div>
  {:else if error}
    <div class="state error">{error}</div>
  {:else}
    <div class="md-body">
      {@html html}
    </div>
  {/if}
</div>

<style>
  .viewer {
    position: fixed;
    inset: 0;
    z-index: 100;
    background: var(--bg-canvas);
    display: flex;
    flex-direction: column;
  }

  .viewer-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 20px;
    background: var(--bg-default);
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
  }

  .viewer-title { font-weight: 600; }

  .close-btn {
    padding: 5px 12px;
    background: var(--bg-subtle);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text-primary);
    cursor: pointer;
    font-size: 13px;
  }

  .close-btn:hover { background: var(--bg-overlay); }

  .state {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
  }

  .state.error { color: var(--accent-red); }

  .md-body {
    flex: 1;
    overflow-y: auto;
    padding: 24px 40px;
    max-width: 900px;
    margin: 0 auto;
    width: 100%;
    line-height: 1.7;
    color: var(--text-primary);
  }

  /* Markdown styles */
  .md-body :global(h1) { font-size: 22px; font-weight: 700; margin: 0 0 16px; color: var(--text-primary); border-bottom: 1px solid var(--border); padding-bottom: 8px; }
  .md-body :global(h2) { font-size: 17px; font-weight: 600; margin: 24px 0 8px; color: var(--text-primary); }
  .md-body :global(h3) { font-size: 15px; font-weight: 600; margin: 16px 0 6px; color: var(--text-muted); }
  .md-body :global(p)  { margin: 0 0 12px; }
  .md-body :global(table) { width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 13px; }
  .md-body :global(th) { padding: 6px 10px; background: var(--bg-subtle); border: 1px solid var(--border); text-align: left; }
  .md-body :global(td) { padding: 6px 10px; border: 1px solid var(--border); }
  .md-body :global(code) { background: var(--bg-subtle); padding: 1px 5px; border-radius: 3px; font-size: 12px; }
  .md-body :global(strong) { color: var(--text-primary); }
  .md-body :global(hr) { border: none; border-top: 1px solid var(--border); margin: 20px 0; }
  .md-body :global(ul), .md-body :global(ol) { padding-left: 20px; margin-bottom: 12px; }
  .md-body :global(li) { margin-bottom: 4px; }
  .md-body :global(blockquote) { border-left: 3px solid var(--accent-blue); margin: 0 0 12px 0; padding: 4px 12px; color: var(--text-muted); }
</style>
