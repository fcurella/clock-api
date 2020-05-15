<script>
	import { clockSocket } from '../stores.js';
  import { alarms } from '../stores.js';
  import { players } from '../stores.js';

  async function commandAlarm(command) {
    //const alarmId = Objects.keys($players)[0];
    const alarmId = Object.keys($alarms)[0];
    if (alarmId === undefined) {
        return;
    }

    const alarm = $alarms[alarmId];
    await $clockSocket.send(JSON.stringify({
      type: command,
      message: alarm,
    }))
  }
  async function snoozeAlarm() {
    await commandAlarm("alarms_snooze");
  }

  async function stopAlarm() {
    await commandAlarm("alarms_stop");
  }
</script>

<div>
  <button class="snooze" on:click|preventDefault={snoozeAlarm}>Snooze</button>
  <button class="stop" on:click|preventDefault={stopAlarm}>Stop</button>
</div>

<style>
    button {
        position: absolute;
        bottom: 15px;
        border-radius: 6px;
        opacity: .5;
        background: transparent;
        color: #859e97;
        padding: 10px 20px;
    }
    .snooze {
        left: 30px;
    }
    .stop {
        right: 30px
    }
</style>
