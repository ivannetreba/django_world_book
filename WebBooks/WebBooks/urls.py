from django.contrib import admin
from django.urls import path, re_path, include
from catalog import views
from catalog.views import BookListView, BookDetailView, AuthorListView, LoanedBooksByUserListView, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    re_path(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', BookDelete.as_view(), name='book_delete'),
    re_path(r'^mybooks/$', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^books/(?P<pk>\d+)$', BookDetailView.as_view(), name='book_detail'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    path('edit1/<int:id>/', views.edit1, name= 'edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('authors_add/', views.authors_add, name='authors_add'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
]
