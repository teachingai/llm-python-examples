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

# 任务描述增加了字段的英文标识符
instruction = """
你的任务是识别用户对手机流量套餐产品的选择条件。
每种流量套餐产品包含三个属性：名称(name)，月费价格(price)，月流量(data)。
根据用户输入，识别用户在上述三种属性上的需求是什么。
"""

# 输出格式增加了各种定义、约束
output_format = """
以JSON格式输出。
1. name字段的取值为string类型，取值必须为以下之一：经济套餐、畅游套餐、无限套餐、校园套餐 或 null；

2. price字段的取值为一个结构体 或 null，包含两个字段：
(1) operator, string类型，取值范围：'<='（小于等于）, '>=' (大于等于), '=='（等于）
(2) value, int类型

3. data字段的取值为取值为一个结构体 或 null，包含两个字段：
(1) operator, string类型，取值范围：'<='（小于等于）, '>=' (大于等于), '=='（等于）
(2) value, int类型或string类型，string类型只能是'无上限'

4. 用户的意图可以包含按price或data排序，以sort字段标识，取值为一个结构体：
(1) 结构体中以"ordering"="descend"表示按降序排序，以"value"字段存储待排序的字段
(2) 结构体中以"ordering"="ascend"表示按升序排序，以"value"字段存储待排序的字段

输出中只包含用户提及的字段，不要猜测任何用户未直接提及的字段，不输出值为null的字段。
"""

# input_text = "办个100G以上的套餐"
# input_text = "有没有便宜的套餐"

# 这条不尽如人意，但换成 GPT-4 就可以了
input_text = "有没有土豪套餐"

prompt = f"""
{instruction}

{output_format}

用户输入：
{input_text}
"""

response = get_completion( prompt, model= dashscope.Generation.Models.qwen_max)
print(response)