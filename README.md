# casher
comfyUI现金宝后端

gunicorn casher.asgi:application --workers 6 --bind 0.0.0.0:8000 --worker-class=uvicorn.workers.UvicornWorker
