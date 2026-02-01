# Automation Exercise 自动化测试实战

本项目基于 Automation Exercise 官方 API/UI 场景，构建接口自动化为主、UI 冒烟为辅的测试工程示例。

## 快速开始

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install
pytest -m api
```

更详细的操作步骤与学习路径请查看：`docs/learning_guide.md`。

## 目录结构

```
configs/               # 环境配置
postman/               # Postman 集合
tests/api/             # API 自动化用例
tests/ui/              # UI 冒烟用例
utils/                 # 公共方法
```

## 用例文档

`docs/testcases.md`
