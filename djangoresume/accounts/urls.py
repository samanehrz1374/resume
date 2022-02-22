from django.urls import path
from accounts import views
from django.conf import  settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('login/',views.loginVeiw,name='login'),
    path('loginpanel/',views.loginpanelview),
    path('logout/',views.logoutVeiw),
    path('profileregister/',views.profileRegisterView),
    path('profile/',views.profileView),
    path('profileEdit/',views.ProfileEditView),
    path('resumeprofile/',views.resumeprofileview),
    path('resumeEdit/',views.ResumeEditView),
    path('loginen/',views.loginen),
    path('password/',views.passwordchangeview),
    # path('password_reset/', views.passwordreset,
    #      name='password_reset'),
    # path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        #  name='password_reset_complete'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)