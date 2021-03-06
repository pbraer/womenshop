from django.urls import path

from shop_app.views import (
    AddToCartView,
    CategoryDetailView,
    BaseView,
    ProductDetailView,
    CartView,
    DeleteFromCartView,
    ChangeQuantityView
)


urlpatterns = [
    path('', BaseView.as_view(), name='mainpage'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQuantityView.as_view(), name='change_qty')
]