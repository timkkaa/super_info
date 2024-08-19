
from django.contrib import admin
from django.urls import path, include
from journal.views import AboutView, HomeView, PublicationView, CreatePublicationCommentView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18/', include('django.conf.urls.i18n')),
]

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('publication/', PublicationView.as_view()),
    path('about/', AboutView.as_view()),
    path('publication-detail/<int:pk>/create-commant/', CreatePublicationCommentView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
