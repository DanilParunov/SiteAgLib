from django.urls import path, include
from .views import *
urlpatterns = [

    path('', list_index, name='list_home'),
    path('create', create, name='create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('library/', library_list_index, name='library'),
    path('library/<int:pk>/', LibDetail.as_view(), name='lib_detail'),
    path('add_book/<int:pk>/', add_book, name='add_book'),
    path('remove_book/<int:book_pk>/<int:customer_pk>', remove_book, name='remove_book'),
]