# 导入依赖库
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 默认使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

# 消息
messages = [
    {
        "role": "system",
        "content": "你是AI助手小瓜，是 AGI 课堂的助教。这门课每周二、四上课。"  # 注入新知识
    },
    {
        "role": "user",
        "content": "人工智能有哪些算法？"  # 问问题。可以改改试试
    },
]

# 调用 GPT-3.5
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# 输出回复
print(chat_completion.choices[0].message.content)