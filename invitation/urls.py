from django.urls import path

from invitation.views import GetInvitationView

urlpatterns = [
    path(
        "invite-code/",
        GetInvitationView.as_view(),
        name="invite_code",
    ),
]
