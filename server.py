import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f'Server Received: {name}')
    greeting = f'Hello {name}!'
    await websocket.send(greeting)
    print(f'Server Sent: {greeting}')

    # Wait for user input to confirm file opening
    input("Press Enter to allow the client to open the file...")  # Block until Enter is pressed
    confirmation = "You can open the file now."
    await websocket.send(confirmation)
    print("Server Sent: File open confirmation.")

async def main():
    async with websockets.serve(hello, "0.0.0.0", 8765):  # Listen on all interfaces
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())

