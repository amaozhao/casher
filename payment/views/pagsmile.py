import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from payment.services import pagsmile_service
from payment.models import PagsmilePayout


class PagsmilePayoutView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user  # 假设用户已通过身份验证
        req_data = request.data
        custom_code = uuid.uuid4()
        payout = pagsmile_service.submit_payout(
            name=req_data.get('name'),
            phone=req_data.get('phone'),
            email=req_data.get('email'),
            account=req_data.get('account'),
            account_type=req_data.get('account_type'),
            custom_code=custom_code,
            fee_bear=req_data.get('fee_bear'),
            amount=req_data.get('amount'),
            source_currency=req_data.get('source_currency'),
            arrival_currency=req_data.get('arrival_currency'),
            additional_remark=req_data.get('additional_remark'),
            country=req_data.get('country')
        )
        if payout.get('data', {}).get('status', None) == "IN_PROCESSING":
            PagsmilePayout.objects.create(
                user=user,
                name=req_data.get('name'),
                phone=req_data.get('phone'),
                email=req_data.get('email'),
                account=req_data.get('account'),
                account_type=req_data.get('account_type'),
                custom_code=custom_code,
                fee_bear=req_data.get('fee_bear'),
                amount=req_data.get('amount'),
                source_currency=req_data.get('source_currency'),
                arrival_currency=req_data.get('arrival_currency'),
                additional_remark=req_data.get('additional_remark'),
                country=req_data.get('country')
            )
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'data': {
                        'custom_code': custom_code,
                        'amount': req_data.get('amount'),
                        'message': '处理中'
                    }
                }
            )
        return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'data': {
                    'custom_code': custom_code,
                    'amount': req_data.get('amount'),
                    'message': '提现失败'
                }
            }
        )


class PagsmileNotify(APIView):

    def post(self, request, *args, **kwargs):
        req_data = request.data
        custom_code = req_data.get('custom_code')
        status = req_data.get('status')
        if status == 'PAID':
            payout = PagsmilePayout.objects.filter(custom_code=custom_code).first()
            if payout:
                payout.status = 'success'
                payout.save()
        return Response(
            {
                'status': status.HTTP_200_OK,
                'data': {
                    'custom_code': custom_code
                }
            }, status=status.HTTP_200_OK
        )
