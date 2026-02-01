import pytest

from utils.config import load_config
from utils.data_factory import user_payload
from utils.http_client import ApiClient


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config()


@pytest.fixture(scope="session")
def api_client(config: dict) -> ApiClient:
    return ApiClient(config["api_base_url"], timeout=config["timeout_seconds"])


def _create_user_with_retry(api_client: ApiClient, max_attempts: int = 3) -> dict:
    last_response = None
    for _ in range(max_attempts):
        payload = user_payload()
        last_response = api_client.post("/createAccount", data=payload)
        try:
            body = last_response.json()
        except Exception:
            body = {}
        if body.get("responseCode") == 201:
            return payload
    pytest.fail(f"Failed to create user after {max_attempts} attempts. Last response: {getattr(last_response, 'text', '')}")


@pytest.fixture
def created_user(api_client: ApiClient) -> dict:
    payload = _create_user_with_retry(api_client)
    yield payload
    api_client.delete(
        "/deleteAccount",
        data={"email": payload["email"], "password": payload["password"]},
    )
