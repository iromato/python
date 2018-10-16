from wsgiref.simple_server import make_server

def smirgo (environ, start_response):
    status = '200 ok'
    headers = [('Content-type','text/plain')]
    start_response(status, headers)

    return ['smirgo te ama']

httpd = make_server('', 8005, smirgo)

print 'Serving on port 8005 ...'

httpd.serve_forever()
