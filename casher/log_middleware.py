import logging


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("django.request")

    def __call__(self, request):
        # 记录请求入参
        self.logger.info(f"Request Path: {request.path}")
        self.logger.info(f"Request Method: {request.method}")
        self.logger.info(f"Request GET Params: {request.GET.dict()}")
        self.logger.info(f"Request POST Params: {request.POST.dict()}")

        if request.body:
            try:
                self.logger.info(f"Request Body: {request.body.decode('utf-8')}")
            except UnicodeDecodeError:
                self.logger.warning("Unable to decode request body")

        response = self.get_response(request)

        # 记录返回的出参
        self.logger.info(f"Response Status Code: {response.status_code}")
        if hasattr(response, "content"):
            self.logger.info(f"Response Content: {response.content.decode('utf-8')}")

        return response
