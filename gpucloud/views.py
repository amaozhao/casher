from rest_framework.response import Response
from rest_framework.views import APIView

from gpucloud.services import gpucloud_service


class GPUCloudView(APIView):
    def post(self, request, *args, **kwargs):
        url = request.data.get("url")
        data = request.data.get("data")
        method = request.data.get("method")
        user = request.user
        resp = gpucloud_service.request_data(url, user, method, data)
        return Response(resp.json(), status=resp.status_code)
