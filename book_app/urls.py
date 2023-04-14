



from django.urls import path
from .views import author_list, book_list
   

urlpatterns = [
    path('', author_list, name='author_list'),
    path('book_list/<int:author_id>/', book_list, name='book_list'),
]
