#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os.path
import logging.handlers

import tornado.web
import tornado.ioloop
import tornado.httpserver

from tornado.options import define, options
from tornado.log import LogFormatter

from urls import urls

# 重写日志输出格式
logger = logging.getLogger()
if options.log_file_prefix:
    logger.handlers = []
    channel = logging.handlers.TimedRotatingFileHandler(
        filename=options.log_file_prefix,
        when='midnight',
        backupCount=options.log_file_num_backups
    )
    channel.setFormatter(LogFormatter(color=False))
    logger.addHandler(channel)

define('application_name', default='luokr', type=str)
define("port", default=10086, help="run on the given port", type=int)


class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            debug=True,
            gzip=True,
            error=False,
            srv='AL/1.0.%s' % int(time.time()),
            login_url='/login',
            xsrf_cookies=True,
            cookie_secret='xc',
            root_path=os.path.join(sys.path[0], 'statics/img'),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "statics"),
        )
        tornado.web.Application.__init__(self, handlers=urls, **settings)


def main():
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
