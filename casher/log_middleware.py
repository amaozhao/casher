import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 记录请求入参
        try:
            request_body = request.body.decode('utf-8') if request.body else ''
            logger.info(f"Request: {request.method} {request.path} | Params: {request_body}")
        except:
            pass

        response = self.get_response(request)

        # 记录响应出参
        try:
            response_body = response.content.decode('utf-8') if response.content else ''
            logger.info(f"Response: {response.status_code} | Body: {response_body[:100]}")
        except:
            pass

        return response
