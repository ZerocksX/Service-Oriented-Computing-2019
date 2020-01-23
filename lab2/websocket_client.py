import websockets
import asyncio
import json


async def send():
    uri = "ws://localhost:5000/board/1"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({'foo': 'bar'}))
        msg = await websocket.recv()
        print(msg)



asyncio.get_event_loop().run_until_complete(send())
