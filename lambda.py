import serverless_wsgi

from serverless_python_example.app import app


def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
