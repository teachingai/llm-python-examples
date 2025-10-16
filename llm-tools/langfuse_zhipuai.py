
# 导入依赖库
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# 初始化 ZhipuAI 客户端
client = ZhipuAI()  # 默认使用环境变量中的 ZHIPUAI_API_KEY 和 ZHIPUAI_BASE_URL


from langfuse.zhipuai import ZhipuAI

from langfuse.decorators import observe
from langfuse.openai import openai  # OpenAI integration


@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a great storyteller."},
            {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    ).choices[0].message.content


@observe()
def main():
    return story()


main()