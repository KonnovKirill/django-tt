from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    # Transaction URLs
    path('', views.TransactionListView.as_view(), name='transaction_list'),
    path('transaction/create/', views.TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction/<int:pk>/update/', views.TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),

    # Dictionary Management URLs
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('status/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('status/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),

    path('types/', views.TypeListView.as_view(), name='type_list'),
    path('type/create/', views.TypeCreateView.as_view(), name='type_create'),
    path('type/<int:pk>/update/', views.TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),

    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('subcategories/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/create/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/update/', views.SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),

    # AJAX URLs
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]
