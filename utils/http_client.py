import requests

from utils.allure_helper import attach_http


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 20) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> requests.Response:
        url = endpoint if endpoint.startswith("http") else f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers,
            timeout=self.timeout,
        )
        attach_http(method, url, params, data, response)
        return response

    def get(self, endpoint: str, params: dict | None = None) -> requests.Response:
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: dict | None = None) -> requests.Response:
        return self.request("POST", endpoint, data=data)

    def put(self, endpoint: str, data: dict | None = None) -> requests.Response:
        return self.request("PUT", endpoint, data=data)

    def delete(self, endpoint: str, data: dict | None = None) -> requests.Response:
        return self.request("DELETE", endpoint, data=data)
