import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f'Server Received: {name}')
    greeting = f'Hello {name}!'
    await websocket.send(greeting)
    print(f'Server Sent: {greeting}')

async def main():
    async with websockets.serve(hello, "0.0.0.0", 8765):  # Listen on all interfaces
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
