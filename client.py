import asyncio
import sys
import uuid
import websockets


async def client_session(client_name):
    uri = "ws://localhost:8000/ws"
    client_id = f"{client_name}-{str(uuid.uuid4())[:4]}"

    async with websockets.connect(uri) as websocket:
        print(f"Client {client_id} connected. Type messages to broadcast (type 'exit' to quit)")
        print("> ", end="", flush=True)

        async def receive_messages():
            while True:
                try:
                    message = await websocket.recv()
                    print(f"\n[Broadcast] {message}")
                    print("> ", end="", flush=True)  # 重新打印输入提示
                except websockets.exceptions.ConnectionClosed:
                    print("\nConnection closed by server")
                    break

        receiver_task = asyncio.create_task(receive_messages())

        try:
            while True:
                message = input()
                if message.lower() == 'exit':
                    break
                await websocket.send(message)
                print("> ", end="", flush=True)  # 发送后重新打印输入提示
        finally:
            receiver_task.cancel()
            try:
                await receiver_task
            except asyncio.CancelledError:
                pass
            print(f"Disconnecting {client_id}...")


if __name__ == "__main__":
    client_name = input("Enter client name: ")
    asyncio.run(client_session(client_name))