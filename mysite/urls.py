"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path , include , re_path
from django.conf import settings
from django.conf.urls.static import static
from website.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap
from django.contrib.auth import views as auth_views
import debug_toolbar 



sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(url address , view)
    path('' , include('website.urls')),
    path('blog/' , include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
    re_path(r'^robots\.txt' , include('robots.urls')),
    path('__debug__/',include(debug_toolbar.urls)),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/' , include('captcha.urls')),
    # ------------------------------------------------------------------------------
    # reset password urls paths 
    path('reset_password/', auth_views.PasswordResetView.as_view(),name="password_reset"), # reset password form

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"), # reset password data sent

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"), # reset password email sent and confirm

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"), # reset password completed
    # ------------------------------------------------------------------------------ 

]

# static (/static/ , base_dir / static)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
