from django.conf.urls import include, url

urlpatterns = [
	url(r'^blog/', include('blog.urls')),
]
