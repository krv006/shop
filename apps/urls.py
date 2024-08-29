from django.urls import path

from apps.views import ProductListCreateAPIView, DebtorsUpdateAPIView, \
    ProductUpdateAPIView, DebtorsListCreateAPIView, CategoryListCreateAPIView, WarehouseListCreateAPIView, \
    ManagerAdminListCreateView, ManagerAdminRetrieveUpdateDestroyView, DailyBenefitView, SaleListCreateAPIView

urlpatterns = [
    path("category", CategoryListCreateAPIView.as_view(), name='category-list-api-view'),

    path("product", ProductListCreateAPIView.as_view(), name='product-list-api-view'),
    path("product/update/<int:pk>", ProductUpdateAPIView.as_view(), name='product-update-list-api-view'),

    path("debtors", DebtorsListCreateAPIView.as_view(), name='debtors-list-api-view'),
    path("debtors/<int:pk>", DebtorsUpdateAPIView.as_view(), name='debtors-update-list-api-view'),

    path("warehouse", WarehouseListCreateAPIView.as_view(), name='warehouse-list-api-view'),

    path('manager-admin/', ManagerAdminListCreateView.as_view(), name='manager-admin-list-create'),
    path('manager-admin/<int:pk>/', ManagerAdminRetrieveUpdateDestroyView.as_view(), name='manager-admin-detail'),

    path('sale/', SaleListCreateAPIView.as_view(), name='sale'),

    path('daily-benefit/<str:date_str>/', DailyBenefitView.as_view(), name='daily_benefit'),
]
