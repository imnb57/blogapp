from django.urls import path
from .views import home, profile, login_view, logout_view,blog_delete, register_view, blog_list, blog_detail, blog_create, blog_edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", home, name="home"),
    path("profile/", profile, name="profile"),
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path('blogs/', blog_list, name='blog_list'),  # List all blogs
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),  # Single blog detail
    path('create/', blog_create, name='blog_create'),  # Create a new blog
    path('edit/<int:blog_id>/', blog_edit, name='blog_edit'),
     path('delete/<int:id>/', blog_delete, name='blog_delete'),  # Delete blog
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
