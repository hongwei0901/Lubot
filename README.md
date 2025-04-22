# LUbot - 智能聊天机器人

基于火山引擎 API 开发的智能聊天机器人应用。

## 功能特点

- 💬 实时对话：支持与 AI 助手进行实时对话
- 🎨 美观界面：现代化的用户界面设计
- 📱 响应式设计：适配各种设备屏幕
- 💾 历史记录：支持保存最近20条对话历史
- 🔄 多功能按钮：支持新建对话、联网搜索、切换模型等功能
- 📎 文件上传：支持上传附件（开发中）

## 安装说明

1. 克隆仓库
```bash
git clone https://github.com/hongwei0901/Lubot.git
cd Lubot
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建 `.env` 文件并添加以下配置：
```
ARK_API_KEY=your_api_key_here
ENDPOINT_ID=your_endpoint_id_here
```

## 使用方法

1. 启动应用
```bash
python app.py
```

2. 在浏览器中访问
```
http://127.0.0.1:5000
```

## 开发计划

- [ ] 添加文件上传功能
- [ ] 支持更多对话模型
- [ ] 添加对话导出功能
- [ ] 优化移动端体验
- [ ] 添加用户认证系统

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。 