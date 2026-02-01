import pytest
from playwright.sync_api import sync_playwright

from utils.data_factory import user_payload
from utils.config import load_config
from utils.http_client import ApiClient


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config()


@pytest.fixture(scope="session")
def ui_base_url(config: dict) -> str:
    return config["ui_base_url"].rstrip("/")


@pytest.fixture(scope="session")
def browser(config: dict):
    headless = config.get("headless", True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


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
    raise AssertionError(
        f"Failed to create user after {max_attempts} attempts. Last response: {getattr(last_response, 'text', '')}"
    )


@pytest.fixture
def ui_user(config: dict) -> dict:
    api_client = ApiClient(config["api_base_url"], timeout=config["timeout_seconds"])
    payload = _create_user_with_retry(api_client)
    yield payload
    api_client.delete(
        "/deleteAccount",
        data={"email": payload["email"], "password": payload["password"]},
    )
