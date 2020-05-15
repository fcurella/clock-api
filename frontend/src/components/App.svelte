<script>
	import {onMount} from 'svelte';
	import { clockSocket } from '../stores.js';

	import { alarms } from '../stores.js';
	import { api_url } from '../stores.js';
	import { players } from '../stores.js';
	import { time } from '../stores.js';

	import AlarmList from "./AlarmList.svelte";
	import DigitalClock from './DigitalClock.svelte';
	import Owl from './Owl.svelte';
	import Controls from './Controls.svelte';

	function arrayToObj(array) {
		return array.reduce((acc, curr) => (acc[curr.id] = curr, acc), {});
	}

	async function loadData() {
		await fetch(`${api_url}/alarms/?active=1`)
			.then(r => r.json())
			.then(items => arrayToObj(items))
			.then((alms) => {
				alarms.set(alms)
		})
	};

	async function removeAlarm(alarm) {
		alarms.update((alms) => (delete alms[alarm.id], alms))
	}

	async function publishAlarm(alarm) {
		if (alarm.active === false) {
			await removeAlarm(alarm);
		} else {
			alarms.update((alms) => (alms[alarm.id] = alarm, alms))
		}
	}

	async function fireAlarm(alarm) {
		const path = alarm.sound.audio;
		const audio = new Audio(path);
		audio.loop = true;
		players.update((pls) => (pls[alarm.id] = audio, pls));

		try {
			await audio.play();
			console.log('Playing...');
		} catch (err) {
			console.log('Failed to play...' + err);
		}
		setTimeout(loadData, 1500);
	}


	async function stopAlarm(alarm) {
		const audio = $players[alarm.id];
		if (audio === undefined) {
			return;
		}
		players.update((pls) => (delete pls[alarm.id], pls))

		try {
			console.log('Stopping...');
			await audio.pause();
		} catch (err) {
			console.log('Failed to stop...' + err);
		}
	}

	function setup() {
		$clockSocket.onopen = loadData;
		$clockSocket.onclose = function(e) {
			console.error('Chat socket closed unexpectedly');
		};

		$clockSocket.onmessage = async function(e) {
			const data = JSON.parse(e.data);
			console.log(data);
			const actions = {
				"alarms_fire": fireAlarm,
				"alarms_publish": publishAlarm,
				"alarms_remove": removeAlarm,
				"alarms_stop": stopAlarm,
			}
			await actions[data.type](data.message);
		};

		return () => {
			$clockSocket.close();
		};
	}
	onMount(setup);
</script>

<main>
	<div class="container">
		<div id="alarms">
			<AlarmList />
		</div>
		<div id="owl">
			<Owl {time} />
		</div>
		<div id="clock">
			<DigitalClock {time} />
		</div>
		<Controls />
	</div>
</main>

<style>
	main {

		xfont-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
	  background: #0e0808;
		height: 100vh;

	}

	.container {
		padding: 5em;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
