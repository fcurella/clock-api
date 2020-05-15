import { readable, writable } from 'svelte/store';
import ReconnectingWebSocket from 'reconnecting-websocket';

export const time = readable(new Date(), set => {
	const interval = setInterval(() => {
		set(new Date());
	}, 1000);

	return () => clearInterval(interval);
});
export const alarms = writable({});
export const players = writable({});

let ws_url = process.env.WS_URL;
if (!ws_url) {
	const protocol = location.protocol === 'https:' ? 'wss' : 'ws';
	ws_url = `${protocol}://${location.host}/ws/alarms/`;
}

export const clockSocket = writable(new ReconnectingWebSocket(ws_url));

export const api_url = process.env.API_URL || '/api';
