from django.urls import path
from users.views import CreateUser, EmailAuth, PasswordResetView, LoginUser, LogoutUser,CommentViewSet
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('registration/', CreateUser.as_view({'post': 'create'}), name='registration'),
    path('email_auth/', EmailAuth.as_view({'post': 'create', 'get': 'get'}), name='email_auth'),
    path('reset_password/', PasswordResetView.as_view({'post': 'create', 'get': 'get'}), name='reset_password'),
    path('login/', LoginUser.as_view({'post': 'login_user'}), name='login'),
    path('logout/', LogoutUser.as_view({'post': 'logout_user'}), name='logout'),
    path('comment_create/', CommentViewSet.as_view({'post': 'create'}, name='comment_create'))
]
