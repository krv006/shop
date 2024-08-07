from django.urls import path

from apps.views import ProductListCreateAPIView, DebtorsUpdateAPIView, \
    ProductUpdateAPIView, DebtorsListCreateAPIView, CategoryListCreateAPIView, WarehouseListCreateAPIView, \
    ManagerAdminListCreateView, ManagerAdminRetrieveUpdateDestroyView, DailyBenefitView

urlpatterns = [
    path("category", CategoryListCreateAPIView.as_view()),

    path("product", ProductListCreateAPIView.as_view()),
    path("product/update/<int:pk>", ProductUpdateAPIView.as_view()),

    path("debtors", DebtorsListCreateAPIView.as_view()),
    path("debtors/<int:pk>", DebtorsUpdateAPIView.as_view()),

    path("warehouse", WarehouseListCreateAPIView.as_view()),

    path('manager-admin/', ManagerAdminListCreateView.as_view(), name='manager-admin-list-create'),
    path('manager-admin/<int:pk>/', ManagerAdminRetrieveUpdateDestroyView.as_view(), name='manager-admin-detail'),

    path('daily-benefit/<str:date_str>/', DailyBenefitView.as_view(), name='daily_benefit'),

]
