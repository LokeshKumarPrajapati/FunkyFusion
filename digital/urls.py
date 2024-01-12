# urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import base_view, home, contact_form, blog_list, edit_blog_post, success_page, services, about_us
from .views import instagram_card
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact_form, name='contact_form'),
    path('blog/', blog_list, name='blog_list'),
    path('edit/<int:post_id>/', edit_blog_post, name='edit_blog_post'),
    path('success/', success_page, name='success_page'),
    path('services/', services, name='services'),
    path('about-us/', about_us, name='about_us'),
    path('base/', base_view, name='base_view'),  # Add the URL for the base_view
    path('instagram-card/', instagram_card, name='instagram_card'),
    

]

# Only serve media files through Django during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


