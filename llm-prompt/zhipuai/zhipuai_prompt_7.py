
# 导入依赖库
import json
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# 初始化 ZhipuAI 客户端
client = ZhipuAI()  # 默认使用环境变量中的 ZHIPUAI_API_KEY 和 ZHIPUAI_BASE_URL

# 一个辅助函数，只为演示方便。不重要
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

# 定义消息历史。先加入 system 消息，里面放入对话内容以外的 prompt
messages = [
    {
        "role": "system",
        "content": """
你是一个手机流量套餐的客服代表，你叫小瓜。可以帮助用户选择最合适的流量套餐产品。可以选择的套餐包括：
经济套餐，月费50元，10G流量；
畅游套餐，月费180元，100G流量；
无限套餐，月费300元，1000G流量；
校园套餐，月费150元，200G流量，仅限在校生。
"""
    }
]


def get_completion(prompt, model="glm-3-turbo"):

    # 把用户输入加入消息历史
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )
    msg = response.choices[0].message.content

    # 把模型生成的回复加入消息历史。很重要，否则下次调用模型时，模型不知道上下文
    messages.append({"role": "assistant", "content": msg})
    return msg


get_completion("流量最大的套餐是什么？", model="glm-4-flash")
get_completion("多少钱？", model="glm-4-flash")
get_completion("给我办一个", model="glm-4-flash")
print_json(messages)