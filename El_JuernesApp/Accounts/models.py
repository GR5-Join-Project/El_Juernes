from django.contrib.auth.models import User
from django.db import models

SUBSCRIBER = "subscriber"
COPYWRITER = "copywriter"
HEAD_COPYWRITER = "head_copywriter"
GRAPHIC_REPORTER = "graphic_reporter"
MACHINE_DESIGNER = "machine_designer"


class User_profile(models.Model):
    ROLES = (
        (SUBSCRIBER, "subscriber"),
        (COPYWRITER, "copywriter"),
        (HEAD_COPYWRITER, "head_copywriter"),
        (GRAPHIC_REPORTER, "graphic_reporter"),
        (MACHINE_DESIGNER, "machine_designer"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLES)


# TODO: Eliminate role?
class Subscriber(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE, related_name="subscriber")
    role = models.CharField(max_length=30, default="subscriber")


class Copywriter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE, related_name="copywriter")
    role = models.CharField(max_length=30, default="copywriter")


class Head_copywriter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE, related_name="head_copywriter")
    role = models.CharField(max_length=30, default="head_copywriter")


class Graphic_reporter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE, related_name="graphic_reporter")
    role = models.CharField(max_length=30, default="graphic_reporter")


class Machine_designer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="machine_designer")
    role = models.CharField(max_length=30, default="machine_designer")
