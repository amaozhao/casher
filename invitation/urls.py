from django.urls import path

from invitation.views import GetInvitationView

urlpatterns = [
    path(
        "invite-url/",
        GetInvitationView.as_view(),
        name="invite_url",
    ),
]
