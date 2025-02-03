from django.urls import path

from . import views

# Aqui, estamos criando uma URL que responde ao método GET na raiz
# ("/") do site
# A função index() é chamada quando essa URL é chamada
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# O Django usa as URLs para direcionar o fluxo de requisições HTTP para as funções de view correspondentes.