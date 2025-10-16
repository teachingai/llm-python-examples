# 导入依赖库
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 默认使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

# 基于 prompt 生成文本
#prompt = "今天我很"
prompt = "今天我很开心，因为"
# 创建一个生成文本的请求
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=100,
    temperature=0,
    stream=True
)

# 迭代响应并打印每个文本块
for chunk in response:  # response 是一个迭代器
    print(chunk.choices[0].text, end='')  # 打印模型生成的文本
