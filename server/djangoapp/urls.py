from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for registration
    path('register', views.registration, name='register'),
    
    # path for login
    path('login', views.login_user, name='login'),
    
    # path for logout
    path('logout', views.logout_user, name='logout'),
    
    # path for dealer reviews view
    path('reviews/<int:dealer_id>/', views.get_dealer_reviews, name='reviews'),
    
    # path for add a review view
    path('add_review', views.add_review, name='add_review'),
    
    # path for dealer details
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
