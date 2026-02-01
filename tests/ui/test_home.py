import allure
import pytest


@allure.title("UI-001 首页核心元素可见")
@pytest.mark.ui
def test_home_page_smoke(page, ui_base_url):
    page.goto(ui_base_url, wait_until="domcontentloaded")
    assert page.title() == "Automation Exercise"
    assert page.locator("img[alt='Website for automation practice']").is_visible()
    assert page.locator("a[href='/login']").is_visible()
