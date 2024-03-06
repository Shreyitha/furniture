from .views import CustomerRegister,CustomerLogin,CategoryGet,CategoryPost,ProductGet,ProductPost ,InvoiceView,get_status_invoice,get_category_product
from django.urls import path
from homeapp import views

urlpatterns=[
    path('customers/',views.CustomerRegister.as_view()),
    path('login/', views.CustomerLogin.as_view(), name='login'),
    path('productget/',views.ProductGet.as_view()),
    path('productpost/',views.ProductPost.as_view()),
    path('categoryget/',views.CategoryGet.as_view()),
    path('categorypost/',views.CategoryPost.as_view()),
    path('invoice/',views.InvoiceView.as_view()),
     path('invoice/<str:status>/', views.get_status_invoice.as_view()),
    path('categoryget/<str:category>/', views.get_category_product.as_view())
   
]
