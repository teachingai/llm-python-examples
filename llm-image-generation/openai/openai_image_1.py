# 导入依赖库
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 ZhipuAI 客户端
client = ZhipuAI()  # 默认使用环境变量中的 ZHIPUAI_API_KEY 和 ZHIPUAI_BASE_URL

# 基于 prompt 生成文本
# 默认使用 cogview-3 模型
def get_completion(prompt, model="cogview-3"):
    response = client.images.generations(
        model=model,  # 填写需要调用的模型名称
        prompt=prompt,
    )
    return response.data[0]          # 返回模型生成的文本


# 调用大模型
response = get_completion("蓝天、白云、绿树、红花。")
print(response)
