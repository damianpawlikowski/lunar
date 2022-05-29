from flask import jsonify


def base_response(status_code, status, msg=None, data=None, data_prefix=None):
    """Base response implemented within JSend convention.
    https://github.com/omniti-labs/jsend
    """
    payload = {}

    payload["status"] = status
    payload["msg"] = msg
    payload["data"] = {}

    if data_prefix is not None:
        payload["data"][data_prefix] = data
    else:
        payload["data"] = data

    response = jsonify(payload)
    response.status_code = status_code

    return response


def error_response(status_code, msg=None, data=None, data_prefix=None):
    """Error response. Should be used whenever request fails due to the server
    internal problems(5xx HTTP status codes)."""
    return base_response(status_code, "error", msg, data, data_prefix)


def fail_response(status_code, msg=None, data=None, data_prefix=None):
    """Fail response. Should be used whenever request fails due to the wrong
    API usage(4xx HTTP status codes)."""
    return base_response(status_code, "fail", msg, data, data_prefix)


def success_response(status_code, msg=None, data=None, data_prefix=None):
    """Success response. Should be used whenever request was processed
    successfully(2xx HTTP status codes)."""
    return base_response(status_code, "success", msg, data, data_prefix)
