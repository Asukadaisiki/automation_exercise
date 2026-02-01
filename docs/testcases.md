# Automation Exercise 测试用例文档

> 说明：用例 ID 与自动化脚本中的 Allure 标题一一对应。

## API 用例

| 用例ID | 标题 | 前置条件 | 测试步骤 | 测试数据 | 断言点 | 预期结果 | 类型 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| API-001 | 产品列表查询 | 无 | GET `/api/productsList` | 无 | responseCode、products 列表 | responseCode=200，返回产品列表 | 回归 |
| API-002 | 产品列表接口方法校验 | 无 | POST `/api/productsList` | 无 | responseCode、message | responseCode=405，提示方法不支持 | 回归 |
| API-003 | 品牌列表查询 | 无 | GET `/api/brandsList` | 无 | responseCode、brands 列表 | responseCode=200，返回品牌列表 | 回归 |
| API-004 | 品牌列表接口方法校验 | 无 | PUT `/api/brandsList` | 无 | responseCode、message | responseCode=405，提示方法不支持 | 回归 |
| API-005 | 搜索产品-正常关键词 | 无 | POST `/api/searchProduct` | search_product=top | responseCode、products | responseCode=200，返回匹配结果 | 回归 |
| API-005-2 | 搜索产品-特殊字符 | 无 | POST `/api/searchProduct` | search_product=@@@### | responseCode、products | responseCode=200，可为空列表 | 回归 |
| API-006 | 搜索产品-缺失参数 | 无 | POST `/api/searchProduct` | 缺少 search_product | responseCode、message | responseCode=400，提示缺参 | 回归 |
| API-007 | 登录校验-正确账号 | 已有用户 | POST `/api/verifyLogin` | email+password | responseCode、message | responseCode=200，用户存在 | 冒烟 |
| API-008 | 登录校验-缺失参数 | 无 | POST `/api/verifyLogin` | 缺少 password 或 email | responseCode、message | responseCode=400，提示缺参 | 回归 |
| API-009 | 登录校验-方法校验 | 无 | DELETE `/api/verifyLogin` | 无 | responseCode、message | responseCode=405，提示方法不支持 | 回归 |
| API-010 | 登录校验-错误账号 | 无 | POST `/api/verifyLogin` | 错误账号密码 | responseCode、message | responseCode=404，用户不存在 | 回归 |
| API-011 | 创建账户 | 无 | POST `/api/createAccount` | 完整用户资料 | responseCode、message | responseCode=201，创建成功 | 冒烟 |
| API-012 | 删除账户 | 已有用户 | DELETE `/api/deleteAccount` | email+password | responseCode、message | responseCode=200，删除成功 | 回归 |
| API-013 | 更新账户 | 已有用户 | PUT `/api/updateAccount` | 修改 city/state | responseCode、message | responseCode=200，更新成功 | 回归 |
| API-014 | 查询账户信息 | 已有用户 | GET `/api/getUserDetailByEmail` | email | responseCode、user | responseCode=200，返回用户信息 | 回归 |

## UI 用例

| 用例ID | 标题 | 前置条件 | 测试步骤 | 测试数据 | 断言点 | 预期结果 | 类型 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UI-001 | 首页核心元素可见 | 无 | 访问首页 | 无 | Logo、登录入口可见 | 首页加载成功 | 冒烟 |
| UI-002 | 产品列表页可访问 | 无 | 进入 Products 页面 | 无 | 标题“All Products”、产品卡片 | 页面渲染成功 | 回归 |
| UI-003 | 搜索产品展示结果 | 无 | Products 页面搜索“top” | search=top | 标题“Searched Products” | 返回搜索结果 | 回归 |
| UI-004 | 登录主流程 | 已有用户 | 登录页输入账号密码并登录 | email+password | “Logged in as”、Logout | 登录成功 | 冒烟 |
