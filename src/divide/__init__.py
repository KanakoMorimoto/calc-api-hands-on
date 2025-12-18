import json
import logging

import azure.functions as func
from src.calc import divide


def _get_param(req: func.HttpRequest, name: str):
    if req.method.lower() == 'post':
        try:
            body = req.get_json()
            if body and name in body:
                return body[name]
        except ValueError:
            pass
    return req.params.get(name)


def _want_html(req: func.HttpRequest) -> bool:
    accept = req.headers.get('Accept', '')
    return 'text/html' in accept and 'application/json' not in accept


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Divide function processed a request.')

    a_raw = _get_param(req, 'a')
    b_raw = _get_param(req, 'b')

    if a_raw is None or b_raw is None:
        body = {"error": "BadRequest", "message": "parameters 'a' and 'b' are required"}
        if _want_html(req):
            return func.HttpResponse(f"<p>{body['message']}</p>", status_code=400, mimetype='text/html')
        return func.HttpResponse(json.dumps(body), status_code=400, mimetype='application/json')

    try:
        result = divide(a_raw, b_raw)
        resp = {"operation": "divide", "a": str(a_raw), "b": str(b_raw), "result": (result if isinstance(result, str) else float(result))}
    except ValueError as e:
        body = {"error": "BadRequest", "message": str(e)}
        if _want_html(req):
            return func.HttpResponse(f"<p>{body['message']}</p>", status_code=400, mimetype='text/html')
        return func.HttpResponse(json.dumps(body), status_code=400, mimetype='application/json')

    if _want_html(req):
        return func.HttpResponse(f"<p>Result: {resp['result']}</p>", status_code=200, mimetype='text/html')
    return func.HttpResponse(json.dumps(resp), status_code=200, mimetype='application/json')
