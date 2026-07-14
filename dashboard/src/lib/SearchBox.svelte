<script>
  let { value = '', onSearch = () => {} } = $props();
</script>

<div class="search-wrap">
  <svg class="search-icon" viewBox="0 0 16 16" width="14" height="14" fill="currentColor">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"/>
  </svg>
  <input
    type="text"
    placeholder="Search company, role, notes…"
    {value}
    oninput={(e) => onSearch(e.target.value)}
  />
</div>

<style>
  .search-wrap {
    position: relative;
    display: flex;
    align-items: center;
  }

  .search-icon {
    position: absolute;
    left: 10px;
    color: var(--text-muted);
    pointer-events: none;
  }

  input {
    width: 100%;
    max-width: 320px;
    padding: 6px 12px 6px 32px;
    background: var(--bg-subtle);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text-primary);
    font-size: 13px;
    outline: none;
    transition: border-color 0.15s;
  }

  input:focus {
    border-color: var(--accent-blue);
  }

  input::placeholder { color: var(--text-muted); }
</style>
