from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template


def Home(request):
    template = get_template("Home.html")

    try:
        user = User.objects.get(username=request.user.username)

        if user.user_profile.role == "subscriber":
            template = get_template("Accounts/Home/subscriber.html")

        elif user.user_profile.role == "copywriter":
            template = get_template("Accounts/Home/copywriter.html")

        elif user.user_profile.role == "head_copywriter":
            template = get_template("Accounts/Home/head_copywriter.html")

        elif user.user_profile.role == "graphic_reporter":
            template = get_template("Accounts/Home/graphic_reporter.html")

        elif user.user_profile.role == "layout_designer":
            template = get_template("Accounts/Home/layout_designer.html")

    except:
        # User not logged or doesn't have a role yet
        # TODO: Redirect to Login Page, not home
        template = get_template("Home.html")

    output = template.render()
    return HttpResponse(output)
