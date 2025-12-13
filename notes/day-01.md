# Day 01 - 启动计划

**挑战链接**: [Advent of Agents - Day 01](https://adventofagents.com/day/1)

## 关键学习

- Advent of Agents 2025 是一个为期 25 天的项目，旨在从零开始构建生产就绪的 Google Cloud AI 智能体
- 该项目涵盖四个主要工具：
  - **Gemini 3**: 上下文工程、计算机使用、实时 API 和高级模式
  - **Google ADK**: 智能体开发工具包（Python）
  - **Vertex AI Agent Engine**: 在几分钟内部署智能体
  - **The Agent Starter Pack**: 端到端生产就绪模板
- 每天提供：一个功能（< 5 分钟试用）、可用的复制粘贴命令，以及文档链接
- 学习路径从快速启动智能体到多智能体编排，从本地开发到生产部署

## 面临的挑战

-
-

## 代码示例

```python
# Day 1 是介绍 - 代码示例将在后续几天出现
# 敬请期待实际实现！
```

## 资源

- [智能体介绍白皮书](http://www.kaggle.com/whitepaper-introduction-to-agents) - 作为 Kaggle 5 天智能体挑战的一部分发布
- [Google ADK 文档](http://google.github.io/adk-docs/) - 智能体开发工具包的官方文档
- [Vertex AI 上的 Agent Engine](http://cloud.google.com/products/agent-builder) - 使用 Vertex AI 大规模部署和管理智能体
- [Agent Starter Pack](http://github.com/GoogleCloudPlatform/agent-starter-pack) - 用于构建 AI 智能体的生产就绪模板

## 问题 / 开放话题

### 什么是 ADK？

**ADK（Agent Development Kit，智能体开发工具包）** 是 Google 的开源、灵活且模块化的框架，用于构建、测试、评估和部署 AI 智能体和多智能体系统。主要特点：

- **代码优先方法**: 直接在代码中定义智能体行为、编排和工具使用
- **模型无关和部署无关**: 针对 Google 生态系统（Gemini、Vertex AI）优化，但可与各种 AI 模型和平台配合使用
- **丰富的工具生态系统**: 预构建工具和支持自定义函数
- **模块化多智能体系统**: 将多个专业智能体组合成灵活的层次结构
- **内置评估和监控**: 日志记录、指标收集和评估工具
- **部署灵活性**: 可以容器化并在本地、云端或通过 Vertex AI Agent Engine 部署
- **多语言支持**: Python、Java 和 Go

ADK 使智能体开发更像传统软件开发，具有模块、工具、测试和监控功能。

**注意**: 与 LLM 无关且可与多个 AI 提供商配合使用的 LangChain 不同，Google ADK 专门针对 Gemini 和 Google 生态系统进行了优化（尽管它可以与其他模型配合使用）。这种优化意味着与 Gemini 特定功能和 Google Cloud 服务的更好集成。

**资源**:
- [官方 ADK 文档](https://google.github.io/adk-docs/)
- [Google Cloud ADK 概述](https://cloud.google.com/agent-builder/agent-development-kit/overview)

### 如何获取 Gemini 3 API 密钥

要获取 Gemini API 密钥：

1. **访问 Google AI Studio**: 前往 [Google AI Studio](https://aistudio.google.com/) 并使用你的 Google 账户登录
2. **创建 API 密钥**:
   - 在导航菜单中点击"获取 API 密钥"
   - 选择在新项目中创建密钥或选择现有的 Google Cloud 项目
   - 你的 API 密钥将立即生成
3. **保护你的 API 密钥**: 复制并安全存储（避免公开分享或嵌入客户端代码）
4. **设置身份验证**: 设置 `GEMINI_API_KEY` 环境变量：
   ```bash
   export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   ```

**重要提示**: 监控你的 API 使用情况，并在 Google Cloud Console 中设置计费警报，以避免意外费用。

**资源**:
- [Google AI for Developers - 设置教程](https://ai.google.dev/tutorials/setup)

### Google AI Studio vs Vertex AI

**Google AI Studio** 和 **Vertex AI** 都是 Google 提供的 AI 平台，但面向不同的使用场景和用户需求：

#### Google AI Studio
- **定位**: 免费的基于 Web 的工具，用于快速原型设计和实验
- **目标用户**: 开发者和非技术用户
- **特点**:
  - 用户友好的界面，无需复杂设置
  - 免费配额：每分钟最多 60 个请求
  - 快速获取 API 密钥，适合快速测试和开发
  - 专注于使用预构建模型进行提示工程和原型开发
- **适用场景**: 原型开发、测试、学习和小型项目

#### Vertex AI
- **定位**: Google Cloud 上全面的、完全托管的 AI 平台
- **目标用户**: 数据科学家和机器学习工程师
- **特点**:
  - 企业级功能：增强的安全性、合规性和数据治理
  - 完整的 ML 生命周期工具：数据准备、模型训练、超参数调优、管道管理
  - 与 Google Cloud 服务的深度集成
  - 按使用量付费模式，适合大规模生产环境
  - 支持自定义模型训练和复杂的 ML 工作流
- **适用场景**: 大规模 AI 项目、生产环境、企业级应用

#### 主要区别总结

| 特性 | Google AI Studio | Vertex AI |
|------|-----------------|-----------|
| **易用性** | 简单，低代码/无代码 | 需要技术专业知识 |
| **定价** | 免费（有配额限制） | 按使用量付费 |
| **功能范围** | 原型设计和实验 | 完整的 ML 生命周期 |
| **企业功能** | 基础 | 企业级（安全、合规） |
| **可扩展性** | 适合小型项目 | 适合大规模生产 |

**选择建议**:
- 如果你刚开始学习、需要快速原型设计或开发小型应用，使用 **Google AI Studio**
- 如果你需要企业级功能、大规模部署、自定义模型训练或复杂的 ML 工作流，使用 **Vertex AI**

两者都提供对 Gemini API 的访问，可以根据项目需求选择合适的平台。
