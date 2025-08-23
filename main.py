import asyncio
import uuid
from fastapi import FastAPI
from fastapi.websockets import WebSocket, WebSocketDisconnect
from typing import Dict

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        client_id = str(uuid.uuid4())
        async with self.lock:
            self.active_connections[client_id] = websocket
        return client_id

    async def disconnect(self, client_id: str):
        async with self.lock:
            if client_id in self.active_connections:
                del self.active_connections[client_id]

    async def broadcast(self, sender_id: str, message: str):
        async with self.lock:
            connections = list(self.active_connections.items())

        tasks = []
        for client_id, connection in connections:
            if client_id != sender_id:
                tasks.append(
                    asyncio.create_task(connection.send_text(f"Client {sender_id}: {message}"))
                )
        if tasks:
            await asyncio.gather(*tasks)


manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    client_id = await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(client_id, data)
    except WebSocketDisconnect:
        await manager.disconnect(client_id)
        await manager.broadcast(client_id, f"Client {client_id} disconnected")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
