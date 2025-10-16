import ollama
response = ollama.generate(
    model="qwen2",
    prompt="天为什么是蓝的?",
    suffix="",
    system="",
    template="",
    context=[],
    stream=False,
    raw=False,
    format="json",       # 响应返回的格式。目前唯一接受的值是 `json`
    images=None,
    options={
        "temperature": 0,                           # 模型输出的随机性，0 表示随机性最小
    },
    keep_alive= 30000
)
print(response['response'])