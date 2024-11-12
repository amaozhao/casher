import logging

logger = logging.getLogger("django")


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 记录请求的输入数据
        logger.info(f"Request: {request.method} {request.path}")
        if request.method == "GET":
            logger.info(f"Form data: {request.GET}")
        if request.method == "POST":
            if request.content_type == "application/x-www-form-urlencoded":
                logger.info(f"Form data: {request.POST}")
            elif request.content_type == "application/json":
                logger.info(f"JSON data: {request.body.decode('utf-8')}")

        response = self.get_response(request)

        # 记录响应的输出数据
        logger.info(f"Response: {response.status_code}")

        if response.status_code == 200:
            logger.info(
                f"Response content: {response.content.decode('utf-8')[:1000]}"
            )  # 限制日志内容的长度

        return response
