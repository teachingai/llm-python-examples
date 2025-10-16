# 导入依赖库
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 默认使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

# 基于 prompt 生成文本
def get_completion(messages, model="gpt-3.5-turbo-1106"):      # 默认使用 gpt-3.5-turbo-1106 模型
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=messages,
        temperature=0,                                  # 模型输出的随机性，0 表示随机性最小
    )
    return response.choices[0].message.content          # 返回模型生成的文本

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    messages = [
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]
    print(get_completion(messages))
