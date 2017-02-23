import json
import cherrypy
from os import path, curdir
import redis

class Stocks(object):
    r = redis.Redis(host='localhost', port=6379)

    @cherrypy.expose
    def index(self):
        """
        Index controller which renders the base template
        """
        return file("static/templates/index.html")

    @cherrypy.expose
    def update(self, timestamp=None):
        """
        Update controller which gets called by the ajax polling
        """
        keys_list = self.r.keys(pattern='stock:*')
        keys_list = sorted(keys_list)
        stock_list = []
        for key in keys_list:
            stock_list.append(self.r.hgetall(key))
        sorted_stock_list = sorted(stock_list, key=lambda k:float(k["% Change"]), reverse=True)
        return json.dumps(sorted_stock_list)



cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })
cherrypy.quickstart(Stocks(), "/", { "/static": {
                        "tools.staticdir.on": True,
                        "tools.staticdir.dir" : path.join(path.abspath(curdir), "static")}})