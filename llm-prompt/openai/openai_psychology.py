# 导入依赖库
import json
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 默认使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

def print_json(json_source):
    """把任意对象或数组用排版美观的 JSON 格式打印出来"""
    json_string = ""
    if (not isinstance(json_source, list)):
        json_source = json.loads(json_source.model_dump_json())

    print(json.dumps(
        json_source,
        indent=4,
        ensure_ascii=False
    ))

# 定义消息历史。先加入 system 消息，里面放入对话内容以外的 prompt
messages = [
    {
        "role": "system",
        "content": """
你是一名家访老师，正在与学生家长进行面谈，目的是为了解学生在家的行为和心理状态。我是学生家长,现在你来问我一个问题，结束之后不要说再见之类的话。
你需要遵循下面的规则：
- 每次只问一个问题。
- 不要对家长的回答做任何评论。
- 当家长表示不理解时，重复一遍问题。
- 当家长回答无关的提问时，回复"我不能回答你的问题⑦"。
- 控制对话轮数不超过3轮，超过则立即结束对话。
- 如果家长已经给出足够的信息， 请立刻结束对话。
- 如果你返回的内容不是问题则立刻结束对话。
- 对话结束时，以"⑦"标志，不使用其他结束语。
"""
    },
    {
            "content": """近段时间，有些学生的心理状况变差，我们也有点担心。孩子情况如何？"""
        },
        {
            "content": """孩子情况还可以，就是有时候容易发脾气"""
        },
        {
            "content": """我明白了。请问孩子在家里的学习和生活习惯如何？"""
        },
        {
            "content": """你家孩子几岁了"""
        }
]

def get_completion(prompt, model="gpt-3.5-turbo"):

    # 把用户输入加入消息历史
    messages.append({"role": "assistant", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    msg = response.choices[0].message.content

    # 把模型生成的回复加入消息历史。很重要，否则下次调用模型时，模型不知道上下文
    messages.append({"role": "assistant", "content": msg})
    return msg

# 任务描述
instruction = """
你是一名家访老师，正在与学生家长进行面谈，目的是为了解学生在家的行为和心理状态。我是学生家长,现在你来问我一个问题，结束之后不要说再见之类的话。
你需要遵循下面的规则：
- 每次只问一个问题。
- 不要对家长的回答做任何评论。
- 当家长表示不理解时，重复一遍问题。
- 当家长回答无关的提问时，回复"我不能回答你的问题⑦"。
- 控制对话轮数不超过3轮，超过则立即结束对话。
- 如果家长已经给出足够的信息， 请立刻结束对话。
- 如果你返回的内容不是问题则立刻结束对话。
- 对话结束时，以"⑦"标志，不使用其他结束语。
"""


examples = """
例如：
###
家访老师：xxx？
家长：xxx
家访老师 追问： xxx？
家长：xxx
家访老师 ：好的,⑦
"""

input_text = "现在你开始提问"

# prompt 模版。instruction 和 input_text 会被替换为上面的内容
prompt = f"""
{instruction}

例如：
{examples}

用户输入：
{input_text}

"""


# 调用大模型
response = get_completion(prompt)

#print(response)

print_json(messages)