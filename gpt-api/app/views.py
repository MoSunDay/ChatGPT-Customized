from datetime import datetime, timedelta, timezone
import json as cjson
import uuid
from sanic import Blueprint, response
from sanic.response import stream, json
import aiohttp
import asyncio

gpt = Blueprint('gpt')
import aiohttp
import asyncio
import json



async def generate_stream(model, prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                response.raise_for_status()
                buffer = ""  # 用于存储不完整的行数据
                async for chunk in response.content:
                    buffer += chunk.decode('utf-8')
                    
                    # 按换行符分割处理完整行
                    while '\n' in buffer:
                        line, buffer = buffer.split('\n', 1)
                        line = line.strip()
                        
                        if not line:
                            continue
                        
                        # 解析JSON
                        try:
                            chunk_data = json.loads(line)
                            text = chunk_data.get('response', '')
                            response = "data: "+ cjson.dumps({
                                "id": f"chatcmpl-{uuid.uuid4()}",
                                "object": "chat.completion.chunk",
                                "created": int(datetime.now(timezone.utc).timestamp()),
                                "model": model,
                                "choices": [{
                                    "index": 0,
                                    "delta": {"content": text},
                                    "finish_reason": None
                                }]
                            }) + "\n\n"
                                # print(char, end='', flush=True)
                                # full_response.append(char)
                            yield response
                        except json.JSONDecodeError as e:
                            print(f"\nJSON解析错误: {e}")
                yield "data: [DONE]\n\n"

    except aiohttp.ClientError as e:
        print(f"请求失败: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

@gpt.route('/v1/chat/completions', methods=["POST"])
async def chat_completions(request):
    req_data = request.json
    content = "".join([item["content"] for item in req_data["messages"][:-1]])
    # model = "deepseek-r1:1.5b"
    model = req_data["model"]
    prompt = f'''
{content}
新提问: {req_data["messages"][-1]["content"]}
'''
    print(model)
    async def streaming_fn(response):
        async for chunk in generate_stream(model, prompt):
            await response.write(chunk)
    return stream(
        streaming_fn,
        content_type='text/event-stream'
    )


if __name__ == '__main__':
    asyncio.run(generate_stream("deepseek-r1:1.5b", "天空为什么是蓝色的"))