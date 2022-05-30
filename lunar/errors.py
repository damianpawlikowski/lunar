from lunar.responses import fail_response


def handle_csrf_error(e):
    """Return CSRF error in the proper API response fromat."""
    return fail_response(400, e.description)
