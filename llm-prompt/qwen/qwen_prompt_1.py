# 导入依赖库
import os
import dashscope
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
        messages=messages,
        result_format='message',  # 将返回结果格式设置为 message
    )
    if response.status_code == HTTPStatus.OK:
        return response.output.choices[0].message.content  # 返回模型生成的文本
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


# 任务描述
instruction = """
你的任务是识别用户对手机流量套餐产品的选择条件。
每种流量套餐产品包含三个属性：名称，月费价格，月流量。
根据用户输入，识别用户在上述三种属性上的倾向。
"""

# 用户输入
input_text = """
办个100G的套餐。
"""

# prompt 模版。instruction 和 input_text 会被替换为上面的内容
prompt = f"""
{instruction}

用户输入：
{input_text}
"""

# 调用大模型
response = get_completion(prompt)
print(response)
