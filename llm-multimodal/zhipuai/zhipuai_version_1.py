# 导入依赖库
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 ZhipuAI 客户端
client = ZhipuAI()  # 默认使用环境变量中的 ZHIPUAI_API_KEY 和 ZHIPUAI_BASE_URL

# 基于 prompt 图片识别
# 默认使用 glm-4v 模型
def get_completion(prompt, model="glm-4v"):
    messages = [{"role": "user", "content": prompt}]    # 将 prompt 作为用户输入
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,                                  # 模型输出的随机性，0 表示随机性最小
    )
    return response.choices[0].message          # 返回模型生成的文本

messages = [
  {
    "type": "text",
    "text": "图里有什么"
  },
  {
    "type": "image_url",
    "image_url": {
        "url": "https://sfile.chatglm.cn/testpath/2b1f6b90-07c0-54b4-8b1a-ecd699aa3b5f_0.png"
    }
  }
]

# 调用大模型
response = get_completion(messages)
print(response)
