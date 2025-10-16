from ollama import generate

response = generate('qwen2', '天为什么是蓝的?')
print(response['response'])
