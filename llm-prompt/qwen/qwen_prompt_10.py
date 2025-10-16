# 导入依赖库
import os
import re
import json
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


def extract_json_from_markdown(markdown_text):
    # 正则表达式匹配JSON对象
    json_pattern = r'```json\n(.*?)\n```'
    matches = re.findall(json_pattern, markdown_text, re.DOTALL)
    json_objects = []
    for match in matches:
        # 去除可能存在的空格和换行
        clean_json = match.strip()
        try:
            # 尝试解析JSON以确认它是有效的
            json.loads(clean_json)
            json_objects.append(clean_json)
        except json.JSONDecodeError:
            # 如果JSON无效，则忽略这个块
            continue
    return json_objects

def performance_analyser(text):
    prompt = f"{text}\n请根据以上成绩，分析候选人在速度、耐力、力量三方面素质的分档。分档包括：强（3），中（2），弱（1）三档。\
                \n以JSON格式输出，其中key为素质名，value为以数值表示的分档。"
    response = get_completion(prompt)
    print("===response===")
    print(response)
    plain_json = extract_json_from_markdown(response)
    print(plain_json)
    return json.loads(plain_json[0])


def possible_sports(talent, category):
    prompt = f"""
        需要{talent}强的{category}运动有哪些。给出10个例子，以array形式输出。确保输出能由json.loads解析。"""
    response = get_completion(prompt)
    print("===response===")
    print(response)
    plain_json = extract_json_from_markdown(response)
    print("===possible_sports===")
    print(plain_json)
    return json.loads(plain_json[0])


def evaluate(sports, talent, value):
    prompt = f"分析{sports}运动对{talent}方面素质的要求: 强（3），中（2），弱（1）。\
                \n直接输出挡位数字。输出只包含数字。"
    response = get_completion(prompt)
    print("===response===")
    print(response)
    val = int(response)
    print(f"{sports}: {talent} {val} {value >= val}")
    return value >= val


def report_generator(name, performance, talents, sports):
    level = ['弱', '中', '强']
    _talents = {k: level[v-1] for k, v in talents.items()}
    prompt = f"已知{name}{performance}\n身体素质：\
        {_talents}。\n生成一篇{name}适合{sports}训练的分析报告。"
    response = get_completion(prompt, model="glm-3-turbo")
    return response


name = "小明"
performance = "100米跑成绩：10.5秒，1500米跑成绩：3分20秒，铅球成绩：12米。"
category = "搏击"

talents = performance_analyser(name+performance)
print("===talents===")
print(talents)

cache = set()
# 深度优先

# 第一层节点
for k, v in talents.items():
    if v < 3:  # 剪枝
        continue
    leafs = possible_sports(k, category)
    print(f"==={k} leafs===")
    print(leafs)
    # 第二层节点
    for sports in leafs:
        if sports in cache:
            continue
        cache.add(sports)
        suitable = True
        for t, p in talents.items():
            if t == k:
                continue
            # 第三层节点
            if not evaluate(sports, t, p):  # 剪枝
                suitable = False
                break
        if suitable:
            report = report_generator(name, performance, talents, sports)
            print("****")
            print(report)
            print("****")