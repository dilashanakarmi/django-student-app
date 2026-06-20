from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('library/', include('library.urls')),
]

# Custom error handlers
handler404 = 'students.views.page_not_found'