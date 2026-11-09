import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

text = "张三，25岁，在长沙做后端，会 Python 和 Java，想找 AI 相关工作"

def extract(text: str) -> dict:
    r = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是信息抽取助手，只输出 JSON，不要任何解释。"},
            {"role": "user", "content": f"从这段话抽取 name, age, city, skills(数组), goal。原文：{text}"},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(r.choices[0].message.content)


if __name__ == "__main__":
    data = extract("张三，25岁，在长沙做后端，会 Python 和 Java，想找 AI 相关工作")
    print(data)
    print("技能：", data.get("skills", []))