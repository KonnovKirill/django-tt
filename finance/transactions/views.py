from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import Status, Type, Category, Subcategory, Transaction
from .forms import StatusForm, TypeForm, CategoryForm, SubcategoryForm, TransactionForm

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
     
        status = self.request.GET.get('status')
        type_id = self.request.GET.get('type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        if status:
            queryset = queryset.filter(status_id=status)
        if type_id:
            queryset = queryset.filter(type_id=type_id)
        if category:
            queryset = queryset.filter(category_id=category)
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction_list')

    def form_valid(self, form):
        messages.success(self.request, 'Транзакция создана успешно.')
        return super().form_valid(form)

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction_list')

    def form_valid(self, form):
        messages.success(self.request, 'Транзакция обновлена успешно.')
        return super().form_valid(form)

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:transaction_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Транзакция удалена успешно.')
        return super().delete(request, *args, **kwargs)


class StatusListView(ListView):
    model = Status
    template_name = 'transactions/dict_list.html'
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'статус'
        context['title'] = 'Статусы'
        context['list_url'] = 'transactions:status_list'
        context['create_url'] = 'transactions:status_create'
        context['update_url'] = 'transactions:status_update'
        context['delete_url'] = 'transactions:status_delete'
        return context

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:status_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = 'transactions:status_list'
        return context

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:status_list')

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'transactions/dict_confirm_delete.html'
    success_url = reverse_lazy('transactions:status_list')

class TypeListView(ListView):
    model = Type
    template_name = 'transactions/dict_list.html'
    context_object_name = 'types'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'тип'
        context['title'] = 'Типы'
        context['list_url'] = 'transactions:type_list'
        context['create_url'] = 'transactions:type_create'
        context['update_url'] = 'transactions:type_update'
        context['delete_url'] = 'transactions:type_delete'
        return context

class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:type_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = 'transactions:type_list'
        return context

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:type_list')

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'transactions/dict_confirm_delete.html'
    success_url = reverse_lazy('transactions:type_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'transactions/dict_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'категория'
        context['title'] = 'Категории'
        context['list_url'] = 'transactions:category_list'
        context['create_url'] = 'transactions:category_create'
        context['update_url'] = 'transactions:category_update'
        context['delete_url'] = 'transactions:category_delete'
        context['show_type'] = True
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = 'transactions:category_list'
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'transactions/dict_confirm_delete.html'
    success_url = reverse_lazy('transactions:category_list')

class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'transactions/dict_list.html'
    context_object_name = 'subcategories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'подкатегория'
        context['title'] = 'Подкатегории'
        context['list_url'] = 'transactions:subcategory_list'
        context['create_url'] = 'transactions:subcategory_create'
        context['update_url'] = 'transactions:subcategory_update'
        context['delete_url'] = 'transactions:subcategory_delete'
        context['show_category'] = True
        return context

class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:subcategory_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = 'transactions:subcategory_list'
        return context

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'transactions/dict_form.html'
    success_url = reverse_lazy('transactions:subcategory_list')

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    template_name = 'transactions/dict_confirm_delete.html'
    success_url = reverse_lazy('transactions:subcategory_list')


# AJAX
def load_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).order_by('name')
    return JsonResponse(list(categories.values('id', 'name')), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)
