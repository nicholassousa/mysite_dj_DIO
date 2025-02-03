from django.urls import path

from . import views

# Aqui, estamos criando uma URL que responde ao método GET na raiz
# ("/") do site
# A função index() é chamada quando essa URL é chamada
app_name = "contacts"
urlpatterns = [
    path("", views.get_name, name="get_name"),
    path("thanks/<str:name>", views.thanks, name="thanks"),  # quando nós incrementamos a função de retornar o nome, nos precisamos de uma URL para isso
    path("create/", views.create, name="create"),
]
