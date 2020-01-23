import asyncio
import websockets
import json

users = {}
clicks = {}


def add_user(path, websocket):
    board_users = users.setdefault(path, [])
    board_users.append(websocket)
    print(f"New user: {websocket}")
    users[path] = board_users


def remove_user(path, websocket):
    board_users = users.setdefault(path, [])
    board_users.remove(websocket)
    print(f"User left: {websocket}")
    users[path] = board_users


def add_click(path, click):
    board_clicks = clicks.setdefault(path, [])
    board_clicks.append(click)
    print(f"New click: path->{path} click->{click}")
    clicks[path] = board_clicks


async def broadcast_click(path, click, without=None):
    if without is None:
        without = []
    board_users = [user for user in users.setdefault(path, []) if user not in without]
    print(f"Broadcasting click: path->{path} click->{click} users->{board_users}")
    if (board_users):
        message = json.dumps([click])
        await asyncio.wait([user.send(message) for user in board_users])


async def send_clicks(path, user):
    print(f"Sending all clicks: path->{path} user->{user}")
    await user.send(json.dumps(clicks.setdefault(path, [])))


async def on_connect(websocket, path):
    add_user(path, websocket)
    await send_clicks(path, websocket)
    try:
        async for message in websocket:
            click = json.loads(message)
            add_click(path, click)
            await broadcast_click(path, click, without=[websocket])
    except Exception as e:
        print(e)
    finally:
        remove_user(path, websocket)


start_server = websockets.serve(on_connect, "0.0.0.0", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
