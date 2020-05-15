from channels.generic.websocket import AsyncJsonWebsocketConsumer


class AlarmsConsumer(AsyncJsonWebsocketConsumer):
    group_name = "alarms"

    async def connect(self):
        self.group_name = "alarms"

        # Join room group
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive_json(self, content):

        # Send message to room group
        await self.channel_layer.group_send(self.group_name, content)

    # Receive message from group
    async def alarms_fire(self, event):
        await self.send_json(event)

    async def alarms_publish(self, event):
        await self.send_json(event)

    async def alarms_remove(self, event):
        await self.send_json(event)

    async def alarms_stop(self, event):
        await self.send_json(event)

    async def alarms_snooze(self, event):
        await self.send_json(event)
