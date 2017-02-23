# -*- coding: utf-8 -*-
import cherrypy
from main import Stocks
import unittest
import urllib

local = cherrypy.lib.httputil.Host('127.0.0.1', 50000, "")
remote = cherrypy.lib.httputil.Host('127.0.0.1', 50001, "")


def setUpModule():
    cherrypy.config.update({'environment': "test_suite"})

    # prevent the HTTP server from ever starting
    cherrypy.server.unsubscribe()

    cherrypy.tree.mount(Stocks(), '/')
    cherrypy.engine.start()
setup_module = setUpModule

def tearDownModule():
    cherrypy.engine.exit()
teardown_module = tearDownModule


class BaseCherryPyTestCase(unittest.TestCase):
    def webapp_request(self, path='/', method='GET', **kwargs):
        headers = [('Host', '127.0.0.1')]
        qs = fd = None
        if method in ['POST', 'PUT']:
            qs = urllib.urlencode(kwargs)
            headers.append(('content-type', 'application/x-www-form-urlencoded'))
            headers.append(('content-length', '%d' % len(qs)))
            fd = StringIO(qs)
            qs = None
        elif kwargs:
            qs = urllib.urlencode(kwargs)

        app = cherrypy.tree.apps['']
        request, response = app.get_serving(local, remote, 'http', 'HTTP/1.1')
        try:
            response = request.run(method, path, qs, 'HTTP/1.1', headers, fd)
        finally:
            if fd:
                fd.close()
                fd = None

        if response.output_status.startswith('500'):
            print response.body
            raise AssertionError("Unexpected error")

        # collapse the response into a bytestring
        response.collapse_body()
        return response


class TestCherryPyApp(BaseCherryPyTestCase):
    def test_index(self):
        response = self.webapp_request('/')
        self.assertEqual(response.output_status, '200 OK')
        
    def test_update(self):
        response = self.webapp_request('/update', timestamp=0)
        self.assertEqual(response.output_status, '200 OK')
        

if __name__ == '__main__':
    import unittest
    unittest.main()