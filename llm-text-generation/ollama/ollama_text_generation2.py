import ollama
response = ollama.chat(model='qwen2', messages=[
  {
    'role': 'user',
    'content': '天为什么是蓝的?',
  },
])
print(response['message']['content'])