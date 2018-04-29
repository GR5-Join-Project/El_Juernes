from django.urls import path
from django.views.generic import TemplateView

from Graphic_reporter import views

urlpatterns = [
    path('noticies_assignades/', views.news_assigned, name="gr_assigned_news"),
    path('banc_imatges/', views.image_bank, name="gr_image_bank"),
    path('banc_imatges/pujar_imatge', views.upload_image, name="gr_upload_image"),

    path('banc_imatges/pujar_imatge/correcte',
         TemplateView.as_view(template_name="Graphic_reporter/correct_upload.html"),
         name="gr_correct_upload"),

    path('banc_imatges/editar_imatge/<int:pk>', views.edit_image, name="gr_edit_image"),

]
