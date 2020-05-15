<script>
  import { beforeUpdate } from 'svelte';

  import { fly } from 'svelte/transition';
	import { time } from '../stores.js';

  export let alarm;
  let inDays;
  let nextFiring;
  let opacity;

  beforeUpdate(() => {
    const currentDate = new Date($time.getFullYear() + '-' + ($time.getMonth() + 1) + '-' + $time.getDate());

    const next = new Date(alarm.next_firing);
    const nextDate = new Date(next.getFullYear() + '-' + (next.getMonth() + 1) + '-' + next.getDate());

    nextFiring = next.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    inDays = (nextDate - currentDate) / (86400 * 1000);
    opacity = (7 - inDays) / 7.0;
  })
</script>

<li
  class="alarm indays-{inDays}"
  transition:fly={{y: -100, duration: 750, opacity: 1, delay: 250}}
  style="opacity: {opacity}"
>
    <time datetime="{alarm.next_firing}">{ nextFiring }</time>
</li>

<style>
    li:before {
        content: "🔔";
    }
</style>
