
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

pip install fastapi uvicorn websockets


## 安装依赖
```bash


给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案