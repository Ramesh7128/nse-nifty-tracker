import json
import cherrypy
from os import path, curdir
import redis
from operator import itemgetter

class StackMirror(object):
    r = redis.Redis(host='localhost', port=6379)

    @cherrypy.expose
    def index(self):
        return file("static/templates/index.html")

    @cherrypy.expose
    def update(self, timestamp=None):
        keys_list = self.r.keys(pattern='stock:*')
        keys_list = sorted(keys_list)
        stock_list = []
        for key in keys_list:
            stock_list.append(self.r.hgetall(key))
        sorted_stock_list = sorted(stock_list, key=lambda k: float(k["% Change"]), reverse=True)
        return json.dumps(sorted_stock_list)



cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 80,
                       })
cherrypy.quickstart(StackMirror(), "/", { "/static": {
                        "tools.staticdir.on": True,
                        "tools.staticdir.dir" : path.join(path.abspath(curdir), "static")}})