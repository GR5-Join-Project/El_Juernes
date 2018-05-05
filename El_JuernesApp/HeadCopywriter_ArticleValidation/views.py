from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from AfeNews.models import New
from Copywriter.models import Article
from HeadCopywriter_ArticleValidation.forms import ArticleComentatForm
from HeadCopywriter_ArticleValidation.models import Article_comentat


# Create your views here.



def Article_validation_list(request):
    template = 'Home_News.html'
    context = None
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/ArticlesToValidate.html'
        context = {
            "articles_alta": New.objects.filter(state="Per validar", priority='alta'),
            "articles_mitjana": New.objects.filter(state="Per validar", priority='mitjana'),
            "articles_baixa": New.objects.filter(state="Per validar", priority='baixa'),
        }
    except:
        template = 'Home_News.html'

    return render(request, template, context)


class Article_validation(generic.DetailView):
    model = New
    context_object_name = 'new_head_copywriter'

    def get_context_data(self, **kwargs):
        context = super(Article_validation, self).get_context_data(**kwargs)
        context['new'] = New.objects.get(slug=self.kwargs['slug'])
        context['article'] = Article.objects.get(slug=self.kwargs['slug'])
        context['form'] = ArticleComentatForm()
        return context

    def get_template_names(self):
        template = 'Home_News.html'
        try:
            user = User.objects.get(username=self.request.user.username)
            rol = user.user_profile.role
            if rol == "Head_copywriter":
                template = 'Head_copywriter/ArticleValidation.html'
        except:
            template = 'Home_News.html'

        return template


# Article acceptat

def Article_accepted(request):
    template = 'Home_News.html'

    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/Correct_Validation.html'
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    if request.method == 'POST':
        var = request.POST.dict()
        name = var['slug'].split('/')

        new = New.objects.get(slug=name[0])
        new.state = "Acceptat"
        new.save()

    return render(request, template)


# Article comentat

def Article_Comentat(request):
    template = 'Home_News.html'

    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/Correct_Validation.html'
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    if request.method == 'POST':
        form = ArticleComentatForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            var = request.POST.dict()
            articleComentat = Article_comentat()
            articleComentat.file = form.clean_file()
            articleComentat.slug = var['slug']
            articleComentat.save()

            new = New.objects.get(slug=var['slug'])
            new.state = "Comentat"
            new.save()

    return render(request, template)


# Article denegat
def Article_rejected(request):
    template = 'Home_News.html'

    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/Correct_Validation.html'
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    if request.method == 'POST':
        var = request.POST.dict()
        name = var['slug'].split('/')

        new = New.objects.get(slug=name[0])
        new.state = "Rebutjada"
        new.save()

    return render(request, template)
