from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .serializers import SiteSerializer
from .models import Site


class UpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'All',
            self.channel_name
        )
        await self.accept()
        sites = Site.objects.all()
        for site in sites:
            serializer = SiteSerializer(site)
            await self.channel_layer.group_send(
                'All',
                {
                    'type': 'chat_message',
                    'message': serializer.data
                }
            )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'All',
            self.channel_name
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
