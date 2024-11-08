#!/bin/bash

# 查找并杀掉所有运行中的 gunicorn 进程
pkill -f 'gunicorn casher.asgi:application'

export http_proxy="http://127.0.0.1:1080"
export https_proxy="http://127.0.0.1:1080"

# 启动新的 gunicorn 进程
gunicorn casher.asgi:application -k uvicorn_worker.UvicornWorker -w 4 -b 0.0.0.0:8000 -D
