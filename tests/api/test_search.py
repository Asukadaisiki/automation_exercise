import allure
import pytest


@allure.title("API-005 搜索产品-正常关键词")
@pytest.mark.api
def test_search_product_valid(api_client):
    response = api_client.post("/searchProduct", data={"search_product": "top"})
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 200
    assert isinstance(payload.get("products"), list)
    assert payload.get("products")


@allure.title("API-005-2 搜索产品-特殊字符")
@pytest.mark.api
def test_search_product_special_characters(api_client):
    response = api_client.post("/searchProduct", data={"search_product": "@@@###"})
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 200
    assert isinstance(payload.get("products"), list)


@allure.title("API-006 搜索产品-缺失参数")
@pytest.mark.api
def test_search_product_missing_param(api_client):
    response = api_client.post("/searchProduct", data={})
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 400
    assert "missing" in payload.get("message", "").lower()
