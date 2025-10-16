import ollama

# 调用 ollama.chat 方法，传入 model='qwen2' 和 messages 参数
response = ollama.chat(model='qwen2', messages=[{
    'role': 'user',
    'content': '天为什么是蓝的?',
  },
])

# 打印模型生成的文本，即 response['message']['content']
print(response['message']['content'])