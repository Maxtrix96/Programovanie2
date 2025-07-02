<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Demo from './Demo.svelte';
  import App2 from './App2.svelte';
  let currentPage = 'home';
</script>

<main>
  <nav>
      <button on:click={() => currentPage = 'home'}>Home</button>
      <button on:click={() => currentPage = 'demo'}>Demo</button>
      <button on:click={() => currentPage = 'app2'}>App2</button>
  </nav>

  {#if currentPage === 'home'}
      <h1>Welcome to the home page</h1>
  {/if}

  {#if currentPage === 'demo'}
      <Demo />
  {/if}

  {#if currentPage === 'app2'}
      <App2 />
  {/if}


  <div>
    <a href="https://vite.dev" target="_blank" rel="noreferrer">
      <img src={viteLogo} class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank" rel="noreferrer">SvelteKit</a>, the official Svelte app framework powered by Vite!
  </p>

  <p class="read-the-docs">
    Click on the Vite and Svelte logos to learn more
  </p>

</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }

  nav {
      margin-bottom: 1rem;
  }

  button {
      margin-right: 0.5rem;
      padding: 8px 12px;
  }
</style>
