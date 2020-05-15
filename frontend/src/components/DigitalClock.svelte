<script>
	import { onMount } from 'svelte';
	export let time;

	const formatter = new Intl.DateTimeFormat('en', {
		hour12: true,
		hour: 'numeric',
		minute: '2-digit',
		second: '2-digit'
	});
	$: parts = formatter.formatToParts($time).reduce((acc, curr) => (acc[curr.type] = curr.value, acc), {})

</script>

<section>
	<div id='' class='clockWrapper'>
		<div class='clockDisplay'>
			{parts.hour}:{parts.minute} <small class="dayPeriod">{parts.dayPeriod}</small>
		</div>
	</div>
</section>

<style>
section, .clockWrapper, .clockDisplay {
  display: flex;
  justify-content: center;
  align-items: center;
}
section{
  overflow: hidden;
  color: #859e97;
}
.clockWrapper {
  width: 75%;
  height: 50%;
	padding: 3em 0;
  border-radius: 15px;
}
.clockDisplay {
	xfont-family: "Fira Code Medium";
  font-size: 5em;
}
	.dayPeriod {
		font-size: 0.3em;
		position: relative;
		line-height: 1;
		top: -.75em;
		padding-left: .25em;
		margin-right: -2.5em
	}
</style>
