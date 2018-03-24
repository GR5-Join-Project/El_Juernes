from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


@login_required
def account_redirect(request):
    return redirect('account-landing', pk=request.user.pk, name=request.user.username)


def Home(request, pk, name):
    template = 'home.html'
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Subscriber":
            template = 'Accounts/Home/subscriber.html'
        elif rol == "Copywriter":
            template = 'Accounts/Home/copywriter.html'
        elif rol == "Head_copywriter":
            template = 'Accounts/Home/head_copywriter.html'
        elif rol == "Graphic_reporter":
            template = 'Accounts/Home/graphic_reporter.html'
        elif rol == "Layout_designer":
            template = 'Accounts/Home/layout_designer.html'

    except:
        template = 'home.html'

    return render(request, template)
