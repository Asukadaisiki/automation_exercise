import allure
import pytest


@allure.title("UI-002 产品列表页可访问")
@pytest.mark.ui
def test_products_page(page, ui_base_url):
    page.goto(f"{ui_base_url}/products", wait_until="domcontentloaded")
    header = page.locator("h2.title.text-center").first
    assert header.inner_text().strip().upper() == "ALL PRODUCTS"
    assert page.locator(".productinfo").count() > 0


@allure.title("UI-003 搜索产品展示结果")
@pytest.mark.ui
def test_search_products(page, ui_base_url):
    page.goto(f"{ui_base_url}/products", wait_until="domcontentloaded")
    page.fill("#search_product", "top")
    page.click("#submit_search")
    header = page.locator("h2.title.text-center").first
    assert header.inner_text().strip().upper() == "SEARCHED PRODUCTS"
    assert page.locator(".productinfo").count() > 0
