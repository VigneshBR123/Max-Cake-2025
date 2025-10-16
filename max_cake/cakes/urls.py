from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('visit_us/', views.VisitorsView.as_view(), name='visit_us'),
    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
    path('add_cake/', views.AddCakeView.as_view(), name='add_cake'),
    path('cake_details/<str:uuid>/', views.CakeDetailsView.as_view(), name='cake_details'),
    path('cake_update/<str:uuid>/', views.CakeUpdateView.as_view(), name='cake_update'),
    path('cake_delete/<str:uuid>/', views.CakeDeleteView.as_view(), name='cake_delete'),
    path('wishlist/', views.WishListView.as_view(), name='cake_wishlist'),
]