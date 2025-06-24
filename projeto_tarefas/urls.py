from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tarefas import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'tarefas', views.TarefaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
