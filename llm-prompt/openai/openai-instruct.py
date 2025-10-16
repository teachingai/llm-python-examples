# 导入Python依赖包
from openai import OpenAI

# 加载 .env 文件到环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 服务。会自动从环境变量加载 OPENAI_API_KEY 和 OPENAI_BASE_URL
client = OpenAI()

# 基于 prompt 生成文本
prompt = "今天我很"  # 改我试试
# prompt = "下班了，今天我很"
# prompt = "放学了，今天我很"
prompt = "AGI 实现了，今天我很"

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