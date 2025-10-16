# 导入依赖库
import json
import requests
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from math import *

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 默认使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

amap_key = "6d672e6194caa3b639fccf2caf06c342"

def print_json(data):
    """
    打印参数。如果参数是有结构的（如字典或列表），则以格式化的 JSON 形式打印；
    否则，直接打印该值。
    """
    if hasattr(data, 'model_dump_json'):
        data = json.loads(data.model_dump_json())

    if (isinstance(data, (list, dict))):
        print(json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ))
    else:
        print(data)

def get_completion(messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # 模型输出的随机性，0 表示随机性最小
        tools=[{
            "type": "function",
            "function": {
                "name": "add_contact",
                "description": "添加联系人",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "联系人姓名"
                        },
                        "address": {
                            "type": "string",
                            "description": "联系人地址"
                        },
                        "tel": {
                            "type": "string",
                            "description": "联系人电话"
                        },
                    }
                }
            }
        }],
    )
    return response.choices[0].message

prompt = "你好"
messages = [
    {"role": "system", "content": "你是wans公司的前台，你的工作是负责询问客户联系发送，并登记客户信息。"},
    {"role": "user", "content": prompt}
]
response = get_completion(messages)
print("=====GPT回复=====")
print_json(response)

while True: # 循环对话

    if (response.tool_calls is None) :
        # 读取字符串
        user_input = input("请输入你的问题：")

        messages.append({"role": "user", "content": user_input})

        response = get_completion(messages)

        print("=====GPT回复=====")
        print_json(response)

        messages.append(response)  # 把大模型的回复加入到对话中

    if (response.tool_calls is not None) :
        # 1106 版新模型支持一次返回多个函数调用请求，所以要考虑到这种情况
        for tool_call in response.tool_calls:
            args = json.loads(tool_call.function.arguments)
            print("=====函数参数展开=====")
            print_json(args)

            if (tool_call.function.name == "add_contact"):

                print("====GPT回复====")
                print_json(response)
                args = json.loads(response.tool_calls[0].function.arguments)
                print("====函数参数====")
                print_json(args)
