import allure
import pytest


@allure.title("API-001 产品列表查询")
@pytest.mark.api
def test_get_products_list(api_client):
    response = api_client.get("/productsList")
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 200
    assert isinstance(payload.get("products"), list)


@allure.title("API-002 POST 产品列表接口不支持")
@pytest.mark.api
def test_post_products_list_not_supported(api_client):
    response = api_client.post("/productsList", data={})
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 405
    assert "not supported" in payload.get("message", "").lower()
