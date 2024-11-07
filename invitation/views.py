from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from invitation.models import InvitationCode


class GetInvitationView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        invition = InvitationCode.objects.filter(inviter=user, accepted=False).first()
        if not invition:
            invition = InvitationCode.objects.create(
                inviter=user,
                code=InvitationCode.generate_raw_code()
            )
        return Response(
            {
                "data": {
                    "invition": invition.key,
                    "status": status.HTTP_200_OK
                }
            }
        )
