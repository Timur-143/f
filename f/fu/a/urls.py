from django.urls import path
from .views import UserDetail, UserList, Mailgb

urlpatterns = [
    path('', Mailgb.as_view()),
    path('user/', UserList.as_view(), name="user")
]