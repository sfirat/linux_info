import os, sys
sys.path.append('.')
def application(environ, start_response):
    status = '200 OK'
    output = 'See you at terokarvinen.com!\n'
    response_headers = [('Content-type', 'text/plain'),
        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]