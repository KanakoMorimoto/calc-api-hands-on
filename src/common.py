import json
from typing import Any, Dict


def json_response(body: Dict[str, Any], status_code: int = 200) -> tuple:
    return (json.dumps(body), status_code, {"Content-Type": "application/json"})


def html_response(html: str, status_code: int = 200) -> tuple:
    return (html, status_code, {"Content-Type": "text/html; charset=utf-8"})
