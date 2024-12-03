from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from gpucloud.services import gpucloud_service


class GPUCloudView(APIView):
    def post(self, request, *args, **kwargs):
        languagestr = request.headers.get('languagestr')
        url = request.data.get("url")
        data = request.data.get("data")
        method = request.data.get("method").lower()
        user = request.user
        resp = gpucloud_service.request_data(url, user, method, data, languagestr=languagestr)
        print(f'gpu response is: {resp.content}')
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
