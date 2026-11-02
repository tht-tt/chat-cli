# chat-cli

一个命令行多轮对话机器人，支持流式输出、上下文管理、对话记录保存。

## 运行

1. 复制 `.env.example` 为 `.env`，填入 DeepSeek API key
2. 安装依赖：`pip install -r requirements.txt`
3. 启动：`python main.py`

## 命令

- `/clear` 清空上下文
- `/save` 保存对话到 chat.md
- `/exit` 退出

## 技术栈

Python + OpenAI SDK + DeepSeek API