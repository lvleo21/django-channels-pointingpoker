from django.urls import path
from apps.pages import views

print(views)
app_name="pages"
urlpatterns = [
    path('lobby/', views.LobbyTemplateView.as_view(), name = "lobby"),
]