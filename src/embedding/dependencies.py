from fastapi import Request


def get_model_dependency(request: Request):
    return request.app.state.model
