import serverless_wsgi

import app

def handler(event, context):
    # app.app - the first app is the the file name, app.py, 
    #           the second app is the VARIABLE inside app.py
    return serverless_wsgi.handle_request(app.app, event, context)