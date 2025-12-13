# Day 02 - Hello World with YAML

**Challenge Link**: [Advent of Agents - Day 02](https://adventofagents.com/day/2)

![Day 02 Screenshot](figs/day-02.png)

## Key Learnings

- 可以在 5 分钟内不使用任何代码构建第一个 AI 智能体
- ADK 支持使用 YAML 配置文件定义智能体，实现快速开发
- 使用 `uvx adk create --type=config` 命令可以快速创建基于 YAML 的智能体项目（无需安装 ADK）
- 生成的 `root_agent.yaml` 文件包含智能体的基本配置（名称、描述、指令、模型）
- 可以使用 `uvx adk web` 命令启动 Web 界面与智能体交互
- 支持使用 Gemini 模型（如 `gemini-2.5-flash` 或 `gemini-3`）
- 使用 `uvx` 可以直接运行 ADK 命令，无需预先安装 `google-adk` 包

## Challenges Faced

- 网站上给的 command 是错误的，运行 `uvx --from google-adk adk web` 时默认时读取 a directory of agents，而不是在 agent directory。

## Code Examples

### 创建 YAML 配置智能体

```bash
# 使用 uvx 创建新的智能体项目（无需安装 ADK）
uvx adk create --type=config agents/my_agent


# 使用 uvx 启动 Web 界面
uvx --from google-adk adk web agents/
```

### root_agent.yaml 示例配置

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk/agents/config_schemas/AgentConfig.json
name: root_agent
description: A helpful assistant for user questions.
instruction: Answer user questions to the best of your knowledge.
model: gemini-2.5-flash
```

## Resources

- [ADK Config Agent Documentation](http://google.github.io/adk-docs/agent/config/) - 使用 YAML 配置构建智能体的文档
- [Tutorial: AI Agent with Google Search (YAML)](http://x.com/Saboo_Shubham_/status/1971038699329908885) - 分步教程（约 2 分钟）
- [Tutorial: Multi-agent app with MCP (YAML)](http://x.com/Saboo_Shubham_/status/1971763476818547010) - 使用 Google ADK 构建多智能体应用
- [Third Party MCP Tools in ADK](http://google.github.io/adk-docs/tool/third-party/) - 将 MCP 工具与 ADK 智能体集成

## Questions / Open Topics

-
-
