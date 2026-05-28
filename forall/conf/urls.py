from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Sem namespace pra usar global
    path('', include('core.urls')),
    path('accounts/', include('profiles.urls')),
    path('projetos/', include('forum.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    
]
