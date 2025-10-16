import ollama

stream = ollama.chat(
    model='qwen2',
    messages=[{'role': 'user', 'content': '天为什么是蓝的?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)