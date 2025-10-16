import ollama

# 调用 ollama.chat 方法，传入 model='qwen2' , messages 参数, stream=True
stream = ollama.chat(
    model='qwen2',
    messages=[{'role': 'user', 'content': '天为什么是蓝的?'}],
    stream=True,
)

# 逐条打印模型生成的文本
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)