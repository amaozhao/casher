import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

# debug = True
loglevel = 'info'
bind = "0.0.0.0:8000"
accesslog = "../log/access.log"
errorlog = "../log/error.log"
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'