import allure
import pytest

from utils.data_factory import user_payload


def _create_account(api_client) -> dict:
    payload = user_payload()
    response = api_client.post("/createAccount", data=payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 201
    return payload


def _delete_account(api_client, payload: dict) -> None:
    api_client.delete(
        "/deleteAccount",
        data={"email": payload["email"], "password": payload["password"]},
    )


@allure.title("API-011 创建账户")
@pytest.mark.api
def test_create_account(api_client):
    payload = user_payload()
    response = api_client.post("/createAccount", data=payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 201
    assert "created" in body.get("message", "").lower()
    _delete_account(api_client, payload)


@allure.title("API-014 查询账户信息")
@pytest.mark.api
def test_get_user_detail(api_client):
    payload = _create_account(api_client)
    response = api_client.get("/getUserDetailByEmail", params={"email": payload["email"]})
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 200
    assert body.get("user", {}).get("email") == payload["email"]
    _delete_account(api_client, payload)


@allure.title("API-013 更新账户信息")
@pytest.mark.api
def test_update_account(api_client):
    payload = _create_account(api_client)
    updated = payload.copy()
    updated["state"] = "CA"
    updated["city"] = "San Francisco"
    response = api_client.put("/updateAccount", data=updated)
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 200
    assert "updated" in body.get("message", "").lower()

    verify = api_client.get("/getUserDetailByEmail", params={"email": payload["email"]})
    assert verify.status_code == 200
    verify_body = verify.json()
    assert verify_body.get("responseCode") == 200
    assert verify_body.get("user", {}).get("state") == "CA"
    assert verify_body.get("user", {}).get("city") == "San Francisco"
    _delete_account(api_client, payload)


@allure.title("API-012 删除账户")
@pytest.mark.api
def test_delete_account(api_client):
    payload = _create_account(api_client)
    response = api_client.delete(
        "/deleteAccount",
        data={"email": payload["email"], "password": payload["password"]},
    )
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 200
    assert "deleted" in body.get("message", "").lower()

    verify = api_client.get("/getUserDetailByEmail", params={"email": payload["email"]})
    assert verify.status_code == 200
    verify_body = verify.json()
    assert verify_body.get("responseCode") == 404
