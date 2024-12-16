from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('inicio2/', views.home2, name='home2'),
    path('content/<int:id>/', views.content_detail, name='content_detail'),
    path('render-json/<int:id>/', views.render_json, name='render_json'),
    path('content/<int:id>/json/', views.render_json, name='render_json'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('crear/', views.create_content, name='create_content'),
    path('crear/<int:id>/', views.create_content, name='create_content'),
    path('cards/', views.content_list, name='content_list'),
    path('cards/<int:id>/', views.content_detail, name='content_detail'),
    path('contenido/', views.listar_contenido, name='listar_contenido'),
    path('delete_content/<int:id>/', views.delete_content, name='delete_content'),
    path('setup-groups/', views.setup_groups, name='setup_groups'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout-to-cuidador/', views.logout_to_cuidador, name='logout_to_cuidador'),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
