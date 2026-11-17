import json, os, re, sys
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field, ValidationError, field_validator

load_dotenv()
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
_client = None

def get_client():
    global _client
    if _client is None:
        key = os.getenv("DEEPSEEK_API_KEY")
        if not key:
            sys.exit("没找到 DEEPSEEK_API_KEY：写进 .env 或先 set 环境变量")
        _client = OpenAI(api_key=key,
                         base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
                         timeout=30, max_retries=2)   # 网络抖动自动重试
    return _client

class Profile(BaseModel):
    name:   str            = Field(description="姓名")
    age:    int | None     = Field(default=None, description="年龄整数，没有就 null")
    city:   str | None     = Field(default=None, description="城市，没有就 null")
    skills: list[str]      = Field(default_factory=list, description="技能，逐个列出，0~5 个")
    goal:   str | None     = Field(default=None, description="求职目标")

    @field_validator("skills", mode="before")
    @classmethod
    def _split(cls, v):
        if v is None:
            return []
        if isinstance(v, str):          # 模型爱把数组写成 "Python、Java"
            return [s for s in re.split(r"[,，、/;；\s]+", v) if s]
        return v

def _clean(raw: str) -> str:
    t = re.sub(r"```(?:json)?", "", raw or "").strip()
    i, j = t.find("{"), t.rfind("}")
    if i < 0 or j <= i:
        raise ValueError(f"输出里没有 JSON 对象：{t[:200]!r}")
    return t[i:j+1]

def extract(text: str, retries: int = 2) -> dict:
    base = [
        {"role": "system", "content":
            "你是信息抽取器，只输出一个 json 对象，不要解释、不要 markdown 代码块。\n"
            "字段必须严格符合这个 JSON Schema：\n"
            + json.dumps(Profile.model_json_schema(), ensure_ascii=False)},
        {"role": "user", "content": f"从这段文本抽取字段：\n<<<\n{text}\n>>>"},
    ]
    msgs, last = base, None
    for _ in range(retries + 1):
        resp = get_client().chat.completions.create(
            model=MODEL, messages=msgs,
            response_format={"type": "json_object"},
            temperature=0, max_tokens=512,        # 0 消随机；给足防截断
        )
        raw = resp.choices[0].message.content or ""
        try:
            return Profile.model_validate(json.loads(_clean(raw))).model_dump()
        except (ValueError, ValidationError) as exc:   # JSONDecodeError 也是 ValueError
            last = exc
            msgs = base + [
                {"role": "assistant", "content": raw},
                {"role": "user", "content": f"上次输出不合格：{str(exc)[:300]}\n只重新输出修正后的 json 对象。"},
            ]
    raise RuntimeError(f"重试 {retries} 次仍失败：{last}")
if __name__ == "__main__":
    samples = [
        "张三，25岁，在长沙做后端，会 Python 和 Java，想找 AI 相关工作",
        "李四，22岁，株洲，应届生，熟悉 Excel 和数据标注",
    ]
    for s in samples:
        print(extract(s))