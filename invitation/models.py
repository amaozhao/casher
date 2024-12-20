import random
import string

from django.contrib.auth.models import User
from django.db import models

s_set = string.ascii_letters + string.digits
raw_code_len = 8


class InvitationCode(models.Model):
    inviter = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=64, unique=True)
    accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def generate_raw_code(cls):
        code = ''.join(random.sample(s_set, raw_code_len))
        while True:
            check = cls.objects.filter(code=code).first()
            if not check:
                return code
            code = ''.join(random.sample(s_set, raw_code_len))

    class Meta:
        db_table = "invitation_code"
        ordering = ["-updated"]


class InvitationRelation(models.Model):
    inviter = models.ForeignKey(
        User, related_name="inviter_relation", on_delete=models.CASCADE
    )
    invitee = models.ForeignKey(
        User, related_name="invitee_relation", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "invitation_relation"
        ordering = ["-updated"]
