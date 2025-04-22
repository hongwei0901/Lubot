import requests
import json

def test_chat(message):
    try:
        response = requests.post(
            'http://127.0.0.1:5000/chat',
            json={'message': message}
        )
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == '__main__':
    test_messages = [
        "你好，请介绍一下你自己",
        "你能做什么？",
        "今天天气怎么样？"
    ]
    
    for msg in test_messages:
        print(f"\n测试消息: {msg}")
        test_chat(msg) 