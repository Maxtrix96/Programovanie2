<script>
  import Demo from './lib/Demo.svelte';
  import App2 from './lib/App2.svelte';
  import DefaultPage from './lib/default_page.svelte';
  import ChatApp from './lib/ChatApp.svelte';
  let currentPage = 'home';
</script>

<header>
  <nav class="navbar">
      <button class="navButton" on:click={() => currentPage = 'home'}>Home</button>
      <button class="navButton" on:click={() => currentPage = 'chat_app'}>Chat App</button>
      <button class="navButton" on:click={() => currentPage = 'demo'}>Demo</button>
      <button class="navButton" on:click={() => currentPage = 'app2'}>Another one</button>
      <button class="navButton" on:click={() => currentPage = 'default_page'}>Default Page</button>
  </nav>
</header>

<main>
  {#if currentPage === 'home'}
      <h1>Welcome to the home page</h1>
  {/if}

  {#if currentPage === 'demo'}
      <Demo />
  {/if}

  {#if currentPage === 'app2'}
      <App2 />
  {/if}

  {#if currentPage === 'default_page'}
      <DefaultPage />
  {/if}

  {#if currentPage === 'chat_app'}
      <ChatApp />
  {/if}
</main>

<style>
  header {
      position: fixed;
      display: flex;
      flex-wrap: wrap;
      width: 100%;
      top: 0;
      left: 0;
      background: rgb(27, 29, 35);
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(97, 97, 109, 0.448); 
      justify-self: center;
      border-radius: 0 0 8px 8px;
  }

  nav {
      padding: 0.5rem 0.5rem;
  }

  .navbar {
      gap: 0.5rem;
      width: 100%;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      align-items: center;
  }
  
  button {
      padding: 8px 12px;
  }

  .navButton {
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: 0.3s ease;
      background-color: transparent;
  }
    .navButton:hover {
        background-color: rgba(255, 255, 255, 0.2);
        color: #fff;
    }
</style>