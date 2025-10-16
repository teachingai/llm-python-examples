# 导入依赖库
import os
import dashscope
import random
from http import HTTPStatus
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 Dashscope 客户端 API-KEY
dashscope.api_key = os.environ.get("DASHSCOPE_API_KEY")

# 基于 prompt 生成文本
# 默认使用 qwen-turbo 模型
def get_completion(prompt, model= dashscope.Generation.Models.qwen_turbo):
    messages = [{"role": "user", "content": prompt}]    # 将 prompt 作为用户输入

    response = dashscope.Generation.call(
        model,
        seed=random.randint(1, 10000), # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
        messages=messages,
        result_format='message',  # 将返回结果格式设置为 message
        presence_penalty=2.0,
    )
    if response.status_code == HTTPStatus.OK:
        return response.output.choices[0].message.content  # 返回模型生成的文本
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_completion('讲个笑话吧'))
