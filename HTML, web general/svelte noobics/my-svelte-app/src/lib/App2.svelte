<script>
    let name = 'World';
    let count = 0;

    function handleClick() {
        count += 1;
    }
</script>

<h1>Hello {name}!</h1>

<input bind:value={name} placeholder="Enter your name" />

<button on:click={handleClick}>
    Clicked {count} {count === 1 ? 'time' : 'times'} 
</button>

{#if count >= 5}
    <p>You're really clicking that button!</p>
{/if}

<style>
    h1 {
        color: #ff3e00;
    }

    button {
        margin-top: 10px;
        padding: 8px 16px;
        font-size: 1rem;
    }
</style>
