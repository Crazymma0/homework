from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from posts import views as posts_views
from blog32.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),

    # posts
    path('', posts_views.main_view),
    path('posts/', posts_views.posts_view),
    path('posts/<int:id>/', posts_views.post_detail_view),
    path('posts/create/', posts_views.post_create_view),

    # hashtags
    path('hashtags/', posts_views.hashtags_view),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)