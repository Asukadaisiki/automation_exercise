import allure
import pytest


@allure.title("API-007 登录校验-正确账号")
@pytest.mark.api
def test_verify_login_valid(api_client, created_user):
    response = api_client.post(
        "/verifyLogin",
        data={"email": created_user["email"], "password": created_user["password"]},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 200
    assert "exists" in payload.get("message", "").lower()


@allure.title("API-008 登录校验-缺失参数")
@pytest.mark.api
def test_verify_login_missing_param(api_client):
    response = api_client.post("/verifyLogin", data={"email": "missing@example.com"})
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 400
    assert "missing" in payload.get("message", "").lower()


@allure.title("API-009 登录校验-DELETE 方法不支持")
@pytest.mark.api
def test_verify_login_delete_not_supported(api_client):
    response = api_client.delete("/verifyLogin", data={})
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 405
    assert "not supported" in payload.get("message", "").lower()


@allure.title("API-010 登录校验-错误账号")
@pytest.mark.api
def test_verify_login_invalid(api_client):
    response = api_client.post(
        "/verifyLogin",
        data={"email": "invalid_user@example.com", "password": "wrong"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload.get("responseCode") == 404
    assert "not found" in payload.get("message", "").lower()
