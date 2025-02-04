import asyncio
import websockets
import os

async def hello():
    uri = "ws://35.222.110.135:8765"  # Replace with the server's public IP
    file_path = input("Drag and drop the file: ")
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f'Client sent: {name}')

        greeting = await websocket.recv()
        print(f"Client received: {greeting}")

        # Wait for server confirmation before opening the file
        print("Waiting for server confirmation to open the file...")
        confirmation = await websocket.recv()
        print(f"Client received: {confirmation}")

        # Open the specified file
        try:
            os.startfile(file_path)  # Open the file using the default program
        except Exception as e:
            print(f"Failed to open file: {e}")

if __name__ == "__main__":
    asyncio.run(hello())
