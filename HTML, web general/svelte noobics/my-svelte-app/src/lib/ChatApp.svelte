<script>
    let prompt = '';
    let response = '';
    let loading = false;
    const maxLength = 100;

    let historyOpen = false;
    let messageHistory = [];

    async function sendPrompt() {
        if (prompt.trim() === '' || prompt.length > maxLength) return;

        loading = true;
        response = '';

        // Fake API call — you can replace this later with a real AI API
        const res = await fetch('https://api.chucknorris.io/jokes/random');
        const data = await res.json();

        response = data.value;
        messageHistory = [
            {
                prompt: prompt.trim(),
                response
            },
            ...messageHistory
        ];
        loading = false;
    }

    function toggleHistory() {
        historyOpen = !historyOpen;
    }
</script>

<div id="chat-app">
    <div class="chat-layout">
        <div class="chat-container">
            <div class="top-bar">
                <h2 id="page-name">Simple AI Prompt UI</h2>
                <button class="history-toggle" on:click={toggleHistory} title="Toggle History">
                    {historyOpen ? '<' : '>'}
                </button>
            </div>
            <div class="input-box">
                <textarea
                    bind:value={prompt}
                    placeholder="Ask something... (doesn't actually call an AI)"
                    maxlength={maxLength} 
                    rows="3"
                ></textarea>
                <div class="history">
                    <p></p>
                </div>
            </div>
            <div>{prompt.length}/{maxLength}</div>
            <button on:click={sendPrompt} disabled={loading || prompt.length === 0}>
                {loading ? 'Thinking...' : 'Send'}
            </button>
            <div class="response-box">
                <p class="response-text">
                {#if prompt === ''}
                    {response = ''} <!-- Reset response if prompt is empty -->
                    <strong>AI response will appear here...</strong>
                {:else if response === ''}
                    <strong>AI response will appear here...</strong>
                {:else}
                    <strong>AI says:</strong> {response}
                {/if}
                </p>
            </div>
        </div>
    </div>
        {#if historyOpen}
        <div class="history-box {historyOpen ? 'open' : ''}">
            <h3>Message History</h3>
            {#if messageHistory.length === 0}
                <p><em>No messages yet</em></p>
            {:else}
                <ul class="history-list">
                    {#each messageHistory as item, index}
                        <li>
                            <strong>Prompt:</strong> {item.prompt}<br />
                            <strong>AI:</strong> {item.response}
                        </li>
                    {/each}
                </ul>
            {/if}
        </div>
        {/if}
</div>

<style>
    textarea {
        width: 100%;
        padding: 8px;
        margin-top: 8px;
        resize: none;
        border-radius: 4px;
    }

    button {
        margin-top: 10px;
        padding: 8px 16px;
    }

    .response-box {
        margin-top: 20px;
        padding: 12px;
        border: 1px solid #ccc;
        background-color: #f9f9f9;
        border-radius: 8px;
        color: black;
        min-width: 100%;
        width: 100%;           /* Ensure it fills the parent width */
        max-width: 100%;       /* Never exceed parent width */
        box-sizing: border-box;/* Include padding/border in width */
        overflow-x: auto;      /* Allow horizontal scroll if needed */
    }


    .response-text {
        margin: 0;
        font-size: 16px;
        line-height: 1.5;
        color: #333;
        word-break: break-word; /* Prevent overflow on long words */
        max-width: 100%;        /* Never exceed parent width */
        box-sizing: border-box;
        overflow-wrap: anywhere;
    }

    .input-box {
        margin-bottom: 0px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        width: 100%;

    }
    
    .input-box textarea {
        flex: 1;
        margin-right: 10px;
    }

    #chat-app {
        position: relative;
        max-width: 500px;
        max-height: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #282c34; 
        color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        overflow: visible;
        padding-bottom: 20px;
    }

    .chat-layout {
        display: flex;
        flex-direction: row;
        align-items: stretch;
        position: relative;
        min-width: 500px;
        max-width: 800px;
    }

    .chat-container {
        flex: 1 1 0;
        min-width: 0;
        z-index: 1;
        display: flex;
        flex-direction: column;
        min-width: 500px; 
    }

    .top-bar {
        display: flex;
        align-items: center;
        justify-content: center; /* Center children horizontally */
        position: sticky;
        top: 0;
        padding: 10px 0;
        border-bottom: 1px solid #ccc;
        z-index: 10;
        gap: 12px; /* Optional: space between children */
    }

    .history-toggle {
        width: 32px;
        height: 32px;
        font-size: 20px;
        text-align: center;
        background-color: #413a3a;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-right: 0;
        flex-shrink: 0; /* Prevent shrinking */
        padding: 0;
    }

    .history-box {
        position: absolute;
        top: 0; 
        right: 0;
        height: calc(100% - 40px); /* match #chat-app padding */
        min-height: 100px;
        width: 300px;
        transform: translate(110%);
        background-color: #414141;
        box-shadow: -2px 0 5px rgba(0, 0, 0, 0.2);
        padding: 1rem;
        z-index: 10;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        pointer-events: auto;
        overflow: hidden;
    }

    .history-box.open {
        transform: translate(110%);
    }

    #page-name {
        margin: 0;
        color: #ffffff;
        flex: 1 1 auto; /* Take up available space */
        text-align: center;
    }

    .history-list {
    list-style: none;
    padding: 0;
    margin-top: 1rem;
    max-height: calc(100% - 60px);
    overflow-y: auto;
    }

    .history-list li {
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #ccc;
    }

</style>
