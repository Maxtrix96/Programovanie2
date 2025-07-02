import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'
import App2 from './App2.svelte'

const app = mount(App, {
  target: document.getElementById('app'),
})

export default app
