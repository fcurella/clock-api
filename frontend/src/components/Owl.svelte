<script>
	import { fade } from 'svelte/transition';
	import { cubicIn, cubicOut } from 'svelte/easing';
	export let time;

  $: msecs = ($time.getSeconds() * 1000) + $time.getMilliseconds();
  $: minutes = $time.getMinutes();

</script>

<div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 733 629">
    <g>
      <path d="M162.64.3c-2.92-.1-5.56,1.64-7.5,3.62C101.64,58.6-36.7,387.15,9.05,629.13H724.28C770,387.15,631.69,58.6,578.19,3.92c-1.94-2-4.58-3.72-7.5-3.62-2.27.08-4.71,1.27-7.06,4.39-24.72,32.68-30.2,67-40.58,100.75-44.39-12-98.26-19.06-156.38-19.06s-112,7.07-156.44,19.06c-10.38-33.79-15.8-68.07-40.52-100.75-2.36-3.12-4.8-4.31-7.07-4.39Z"/>
      <path class="owl-nose" d="M365.05,461.41c-7.37.15-37.24,1.59-42.93,14.57-11.5,26.24,36.67,96.46,44.57,94.62,7.91,1.84,56-68.38,44.52-94.62-6.5-14.84-44.52-14.57-44.52-14.57S366.1,461.39,365.05,461.41Z" style="fill: rgb(206, 199, 195)"/>
      {#if (minutes % 3 != 0 || msecs >= 50)}
      <g out:fade={{duration: 50, easing: cubicOut}} in:fade={{duration: 200, easing: cubicIn}}>
        <path class="owl-eye owl-eye-left" d="M198,247.59A112.66,112.66,0,1,0,310.71,360.22,112.57,112.57,0,0,0,198,247.59Zm0,170.89a58.24,58.24,0,1,1,58.26-58.26A58.23,58.23,0,0,1,198,418.48Z" style="fill: #f95"/>
      </g>
      {/if}
      {#if (minutes % 5 != 0 || msecs >= 50)}
      <g out:fade={{duration: 50, easing: cubicOut}} in:fade={{duration: 200, easing: cubicIn}}>
        <path class="owl-eye owl-eye-right" d="M535.26,247.59c-148.08,2.52-148,222.8,0,225.32C683.3,470.37,683.32,250.09,535.26,247.59Zm0,170.89c-76.1-.34-76.14-116.15,0-116.47C611.87,303.32,611.81,417.17,535.26,418.48Z" style="fill: #f95"/>
      </g>
      {/if}
    </g>
  </svg>
</div>


<style>
    div {
        text-align: center;
    }
    svg {
        height: 50vh;
    }
</style>
