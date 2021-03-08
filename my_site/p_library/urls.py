from django.urls import path
from p_library import views

app_name = 'p_library'  

urlpatterns = [
    path('books_json', views.books_json),
    path('books', views.books_list, name='books'),
    path('books/send', views.BookSend.as_view(), name='book_send'),

    path('publishers', views.publisher_list, name='publishers'),

    path('friend/create', views.FriendAdd.as_view(), name='friend_create'),  
    path('friends', views.FriendList.as_view(), name='friend_list'),
    path('friends/<int:pk>', views.FriendDetail.as_view(), name='friend_detail'),
  
]


# path('', views.books_list),
#     path('index/', views.index, name='books'),
#     path('index/book_increment/', views.book_increment),
#     path('index/book_decrement/', views.book_decrement),
#     path('publishers', views.publisher_list, name='publishers'),
# ]