import allure
import pytest


@allure.title("UI-004 登录主流程")
@pytest.mark.ui
def test_login_flow(page, ui_base_url, ui_user):
    page.goto(f"{ui_base_url}/login", wait_until="domcontentloaded")
    page.fill("[data-qa='login-email']", ui_user["email"])
    page.fill("[data-qa='login-password']", ui_user["password"])
    page.click("[data-qa='login-button']")
    page.wait_for_selector("text=Logged in as", timeout=15000)
    assert page.locator("a[href='/logout']").is_visible()
