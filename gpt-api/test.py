import aiohttp
import asyncio
import json



async def main():
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "deepseek-r1:1.5b",
        "prompt": "为什么天空是蓝色的？",
        "stream": True
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                response.raise_for_status()

                buffer = ""  # 用于存储不完整的行数据
                full_response = []

                # 逐块读取响应内容
                async for chunk in response.content:
                    # 将字节解码为字符串并与缓冲区合并
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
                            
                            # 逐字输出
                            for char in text:
                                print(char, end='', flush=True)
                                full_response.append(char)
                                
                        except json.JSONDecodeError as e:
                            print(f"\nJSON解析错误: {e}")

                # 打印最终合并结果
                print("\n完整回答:", ''.join(full_response))

    except aiohttp.ClientError as e:
        print(f"请求失败: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

# 运行异步主函数
if __name__ == "__main__":
    asyncio.run(main())