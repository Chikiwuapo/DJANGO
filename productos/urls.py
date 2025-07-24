from django.urls import path
from .views import (
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
)

urlpatterns = [
    # Productos
    path('', ProductoListView.as_view(), name='producto_list'),
    path('producto/nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
    # Categorías
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/nueva/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),
] 