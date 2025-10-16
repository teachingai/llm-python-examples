import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import os
import asyncio

# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# 创建 semantic kernel
kernel = sk.Kernel()

# 配置 OpenAI 服务
api_key = os.getenv('OPENAI_API_KEY')
endpoint = os.getenv('OPENAI_BASE_URL')

print('endpointxxxx', endpoint)

model = OpenAIChatCompletion(
    "gpt-3.5-turbo", api_key, endpoint=endpoint)
# "gpt-3.5-turbo", api_key)

kernel.add_text_completion_service("my-gpt3", model)

# 定义 semantic function
# 参数由{{ }}标识
tell_joke_about = kernel.create_semantic_function("给我讲个关于{{$input}}的笑话吧")


# 运行 function 看结果
async def run_function():
    result = await kernel.run_async(
        tell_joke_about,
        input_str="Hello world"
    )
    print(result)


asyncio.run(run_function())