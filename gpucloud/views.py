from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import logging

from gpucloud.services import gpucloud_service


logger = logging.getLogger("django")


class GPUCloudView(APIView):
    def post(self, request, *args, **kwargs):
        languagestr = request.headers.get('languagestr')
        url = request.data.get("url")
        data = request.data.get("data")
        method = request.data.get("method").lower()
        user = request.user
        resp = gpucloud_service.request_data(url, user, method, data, languagestr=languagestr)
        logger.info(f"GPU response is: {resp}")
        return Response(resp.json(), status=resp.status_code)


class GPUCloudTokenView(APIView):
    def post(self, request, *args, **kwargs):
        current_user = request.user
        gpu_token = gpucloud_service.get_token(current_user, True)
        return Response(
            {
                'data': {
                    'gpu_token': gpu_token,
                },
                'status': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
