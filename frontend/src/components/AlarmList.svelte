<script>
	import { alarms } from '../stores.js';
	import Alarm from './Alarm.svelte';

	$: alarmList = Object.values($alarms).sort(
	    (a, b) => new Date(a.next_firing) - new Date(b.next_firing)
  );

</script>

<ul>
  {#each alarmList as alarm (alarm.id)}
  <Alarm {alarm} />
  {/each}
</ul>

<style>
    ul {
        position: absolute;
        list-style-type: none;
        padding: 0;
        margin: 0;
    }
</style>
