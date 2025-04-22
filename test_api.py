import requests
import json
import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# API配置
API_KEY = "68d6a4cf-460b-4d77-b9b8-7b2815d30392"
API_URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
ENDPOINT_ID = "ep-20250422113328-qhhzm"

def test_api():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": ENDPOINT_ID,
        "messages": [
            {"role": "system", "content": "你是一个智能助手，请用中文回答用户的问题。"},
            {"role": "user", "content": "你好"}
        ],
        "temperature": 0.7,
        "max_tokens": 2000
    }
    
    try:
        logger.info("开始测试API连接...")
        logger.debug(f"请求头: {headers}")
        logger.debug(f"请求体: {payload}")
        
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        logger.info(f"状态码: {response.status_code}")
        logger.info(f"响应内容: {response.text}")
        
        if response.status_code == 200:
            print("API连接测试成功！")
        else:
            print(f"API请求失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
            
    except requests.exceptions.SSLError as e:
        print(f"SSL错误: {str(e)}")
    except requests.exceptions.ConnectionError as e:
        print(f"连接错误: {str(e)}")
    except requests.exceptions.Timeout as e:
        print(f"请求超时: {str(e)}")
    except Exception as e:
        print(f"未知错误: {str(e)}")

if __name__ == "__main__":
    test_api() 