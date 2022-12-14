from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, ChangePasswordForm, ResetPasswordForm, MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_to_cart, name='cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/<str:category>/<str:data>', views.mobile, name='mobile'),
    path('all_product/<slug:data>', views.all_product, name='all_product'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('edit_product/', views.edit_product, name='edit_product'),
    # User Authentication Urls
    path('registration/', views.UserRegistration.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login.html",authentication_form=LoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name="app/change_password.html",form_class=ChangePasswordForm,success_url='/passwordchangedone/'),name="passwordchange"),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name="app/change_password_done.html"),name="passwordchangedone"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="app/password_reset.html",form_class=ResetPasswordForm),name="password-reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html",form_class=MySetPasswordForm),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"),name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
