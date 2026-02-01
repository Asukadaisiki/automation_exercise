# 操作与学习指南

> 本文档用于从零搭建环境、运行测试、阅读用例与扩展脚本。

## 1. 环境准备

- Python 3.10+（推荐）
- Node.js 18+（Playwright 安装浏览器需要）
- Git（可选）
- Allure CLI（可选，用于可视化报告）

## 2. 项目结构速览

```
automation_exercise
├── configs/                # 环境与配置
├── docs/                   # 用例与学习文档
├── postman/                # Postman 集合与环境
├── tests/                  # pytest 用例（api/ui）
├── utils/                  # 公共方法
└── .github/workflows       # CI 配置
```

## 3. 安装依赖

建议使用虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

安装 Playwright 浏览器：

```powershell
python -m playwright install
```

## 4. 配置说明

默认配置在 `configs/config.json`：

- `base_url`：站点根地址
- `api_base_url`：API 根地址
- `ui_base_url`：UI 根地址
- `timeout_seconds`：请求超时
- `headless`：UI 测试是否无头

你也可以通过环境变量覆盖（示例见 `configs/.env.example`）。

## 5. 运行 API 自动化

只跑 API：

```powershell
pytest -m api
```

或指定目录：

```powershell
pytest tests/api
```

生成 Allure 报告（可选）：

```powershell
pytest -m api --alluredir=allure-results
allure serve allure-results
```

## 6. 运行 UI 冒烟

```powershell
pytest -m ui
```

如果需要可视化浏览器，将 `configs/config.json` 中的 `headless` 改为 `false`。

## 7. 使用 Postman 联调

1. 导入 `postman/collection.json`
2. 导入 `postman/environment.json`
3. 运行 Create Account 请求，会自动生成 `user_email`
4. 再依次运行 Verify/Login、Update、Get、Delete

## 8. 用例与脚本映射规则

- 用例文档：`docs/testcases.md`
- 脚本文件：`tests/api/*`、`tests/ui/*`
- Allure 标题与用例 ID 一致（例如：API-001）

## 9. 扩展新用例的建议流程

1. 在 `docs/testcases.md` 中补充用例
2. 在 `tests/api` 或 `tests/ui` 新增脚本
3. 在断言中关注 responseCode / message / 关键字段
4. 如果用到账号数据，优先复用 `utils/data_factory.py`

## 10. 常见问题

- **账号重复导致创建失败**：用例已使用随机邮箱，重复概率极低
- **UI 用例失败**：确认网络正常，必要时改为 `headless=false` 观察
- **Allure 无法启动**：确认已安装 Allure CLI（需 Java 环境）

## 11. CI 说明

默认 GitHub Actions 只运行 API 用例，UI 用例可按需手动触发。
