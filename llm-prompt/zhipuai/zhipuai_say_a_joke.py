
# 导入依赖库
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# 初始化 ZhipuAI 客户端
client = ZhipuAI()  # 默认使用环境变量中的 ZHIPUAI_API_KEY 和 ZHIPUAI_BASE_URL

# 基于 prompt 生成文本
def get_completion(prompt, model="glm-3-turbo"):      # 默认使用 glm-3-turbo 模型
    messages = [{"role": "user", "content": prompt}]    # 将 prompt 作为用户输入
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,                                  # 模型输出的随机性，0 表示随机性最小
    )
    return response.choices[0].message.content          # 返回模型生成的文本

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_completion('讲个笑话'))
