# 导入依赖库
import ollama

# 基于 prompt 生成文本
# 默认使用 qwen2 模型
def get_completion(prompt, response_format="json", model="qwen2"):
    messages = [{"role": "user", "content": prompt}]    # 将 prompt 作为用户输入
    response = ollama.generate(
        model=model,
        prompt=messages,
        #tools: Optional[Sequence[Tool]] = None,
        stream=False,
        #format=response_format,                         # 响应返回的格式。目前唯一接受的值是 `json`
        # options={
        #     "temperature": 0,                           # 模型输出的随机性，0 表示随机性最小
        # },
        keep_alive= 30000,
    )
    return response         # 返回模型生成的文本

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
