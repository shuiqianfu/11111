
### 使用说明
1. 安装依赖：`pip install fastapi uvicorn websockets`
2. 启动服务端：`uvicorn main:app --reload` 
3. 启动多个客户端：`python client.py` 
4. 在客户端输入任意消息，观察广播效果
5. 输入"exit"退出客户端

这个实现满足所有要求：
1. 使用FastAPI+WebSockets处理多客户端连接
2. 使用UUID为每个连接分配唯一标识
3. 实现广播机制
4. 包含完整的运行说明和示例
5. 代码结构清晰简洁

客户端界面会显示：

# WebSocket 广播系统

## 功能说明
- 服务端支持多客户端连接，为每个连接分配唯一ID
- 客户端发送的消息会广播给所有其他客户端
- 客户端断开连接时会通知其他客户端

## 环境要求
- Python 3.7+
- 依赖包: `fastapi`, `uvicorn`, `websockets`

## 安装依赖
```bash
pip install fastapi uvicorn websockets