import os
import httpx
from volcenginesdkarkruntime import Ark
import time

class ChatBot:
    def __init__(self, api_key, endpoint_id):
        self.api_key = api_key
        self.endpoint_id = endpoint_id
        self.client = Ark(
            api_key=api_key,
            timeout=httpx.Timeout(timeout=1800),
        )
        self.conversation_history = []

    def chat(self, user_input):
        # 添加用户输入到历史记录
        self.conversation_history.append({"role": "user", "content": user_input})
        
        print("\n机器人正在思考...\n")
        
        # 使用流式输出
        stream = self.client.chat.completions.create(
            model=self.endpoint_id,
            messages=self.conversation_history,
            stream=True
        )
        
        assistant_response = ""
        print("机器人: ", end="")
        for chunk in stream:
            if not chunk.choices:
                continue
            if chunk.choices[0].delta.reasoning_content:
                content = chunk.choices[0].delta.reasoning_content
                print(content, end="")
                assistant_response += content
            else:
                content = chunk.choices[0].delta.content
                print(content, end="")
                assistant_response += content
        
        # 添加助手回复到历史记录
        self.conversation_history.append({"role": "assistant", "content": assistant_response})
        print("\n")

def main():
    # 设置API密钥
    api_key = "68d6a4cf-460b-4d77-b9b8-7b2815d30392"
    endpoint_id = "ep-20250422113328-qhhzm"
    
    # 创建聊天机器人实例
    bot = ChatBot(api_key, endpoint_id)
    
    print("欢迎使用火山引擎聊天机器人！")
    print("输入 'quit' 或 'exit' 退出对话")
    print("-" * 50)
    
    while True:
        user_input = input("\n你: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("再见！")
            break
            
        if user_input.strip():
            bot.chat(user_input)

if __name__ == "__main__":
    main()
