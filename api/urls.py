from .views import Movieapiview, Movieapilistview
from django.urls import path

urlpatterns = [
    path('movieapi/list/', Movieapilistview.as_view(), name='movieapilist'),
    path('movieapi/<int:id>/', Movieapiview.as_view(), name='movieapiobject'),
]
