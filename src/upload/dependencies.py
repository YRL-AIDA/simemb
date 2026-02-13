from fastapi import Request


def get_upload_deps(request: Request):
    return request.app.state.settings
