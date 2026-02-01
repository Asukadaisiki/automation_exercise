import json
import os
from pathlib import Path

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "config.json"


def load_config(path: str | None = None) -> dict:
    config_path = Path(path) if path else DEFAULT_CONFIG_PATH
    with open(config_path, "r", encoding="utf-8-sig") as handle:
        cfg = json.load(handle)

    cfg["base_url"] = os.getenv("BASE_URL", cfg.get("base_url", ""))
    cfg["api_base_url"] = os.getenv(
        "API_BASE_URL",
        cfg.get("api_base_url") or f"{cfg['base_url'].rstrip('/')}/api",
    )
    cfg["ui_base_url"] = os.getenv("UI_BASE_URL", cfg.get("ui_base_url", cfg["base_url"]))

    cfg["timeout_seconds"] = int(os.getenv("HTTP_TIMEOUT", cfg.get("timeout_seconds", 20)))
    headless_raw = os.getenv("HEADLESS", str(cfg.get("headless", True)))
    cfg["headless"] = str(headless_raw).lower() in {"1", "true", "yes", "y"}

    return cfg
