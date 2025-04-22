from quart import Quart, render_template, request, jsonify
import logging
import os
import requests
import json

# 配置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Quart(__name__)

# 设置API Key
API_KEY = os.getenv("ARK_API_KEY", "68d6a4cf-460b-4d77-b9b8-7b2815d30392")
ENDPOINT_ID = "ep-20250422113328-qhhzm"
API_URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

@app.route('/')
async def index():
    return await render_template('index.html')

@app.route('/chat', methods=['POST'])
async def chat():
    data = await request.get_json()
    user_message = data.get('message', '')
    
    try:
        logger.debug(f"发送消息到API: {user_message}")
        
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": ENDPOINT_ID,
            "messages": [
                {"role": "system", "content": "你是一个智能助手，请用中文回答用户的问题。"},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=120
        )
        
        if response.status_code == 200:
            response_data = response.json()
            response_content = response_data["choices"][0]["message"]["content"]
            logger.debug(f"API响应内容: {response_content}")
            return jsonify({"response": response_content})
        else:
            error_msg = f"API请求失败，状态码: {response.status_code}, 响应: {response.text}"
            logger.error(error_msg)
            return jsonify({"error": error_msg}), response.status_code
    
    except requests.exceptions.SSLError as e:
        error_msg = f"SSL错误: {str(e)}"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 500
    except requests.exceptions.ConnectionError as e:
        error_msg = f"连接错误: {str(e)}"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 500
    except requests.exceptions.Timeout as e:
        error_msg = f"请求超时: {str(e)}"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 504
    except Exception as e:
        error_msg = f"未知错误: {str(e)}"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) 