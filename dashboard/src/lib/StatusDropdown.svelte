<script>
  import { updateStatus } from './api.js';

  let { app = null, onSaved = () => {} } = $props();

  const STATUSES = ['evaluated', 'applied', 'responded', 'interview', 'offer', 'rejected', 'discarded', 'skip'];

  let saving   = $state(false);
  let saved    = $state(false);
  let errorMsg = $state('');

  async function handleChange(e) {
    const newStatus = e.target.value;
    if (!app?.reportNumber || newStatus === app.statusNorm) return;

    saving = true;
    saved = false;
    errorMsg = '';

    try {
      await updateStatus(app.reportNumber, app.status, newStatus);
      saved = true;
      setTimeout(() => { saved = false; }, 2000);
      onSaved(newStatus);
    } catch (err) {
      errorMsg = err.message;
    } finally {
      saving = false;
    }
  }
</script>

<div class="dropdown-wrap">
  <label class="dropdown-label">Status</label>
  <div class="select-row">
    <select
      value={app?.statusNorm ?? ''}
      onchange={handleChange}
      disabled={saving || !app?.reportNumber}
    >
      {#each STATUSES as s}
        <option value={s}>{s.charAt(0).toUpperCase() + s.slice(1)}</option>
      {/each}
    </select>

    {#if saving}
      <span class="indicator saving">Saving…</span>
    {:else if saved}
      <span class="indicator saved">✓ Saved</span>
    {:else if errorMsg}
      <span class="indicator error">{errorMsg}</span>
    {/if}
  </div>

  {#if !app?.reportNumber}
    <p class="no-report">No report linked — status cannot be updated.</p>
  {/if}
</div>

<style>
  .dropdown-wrap { display: flex; flex-direction: column; gap: 4px; }

  .dropdown-label {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    color: var(--text-muted);
  }

  .select-row { display: flex; align-items: center; gap: 8px; }

  select {
    flex: 1;
    padding: 6px 10px;
    background: var(--bg-subtle);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text-primary);
    font-size: 13px;
    cursor: pointer;
    outline: none;
  }

  select:focus { border-color: var(--accent-blue); }
  select:disabled { opacity: 0.5; cursor: not-allowed; }

  .indicator { font-size: 12px; white-space: nowrap; }
  .saving { color: var(--text-muted); }
  .saved  { color: var(--accent-green); }
  .error  { color: var(--accent-red); }

  .no-report { font-size: 11px; color: var(--text-muted); margin: 0; }
</style>
