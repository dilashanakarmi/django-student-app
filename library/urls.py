from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    MemberListView, MemberDetailView, MemberCreateView, MemberUpdateView, MemberDeleteView,
    BorrowRecordListView, BorrowRecordDetailView, BorrowRecordCreateView, BorrowRecordUpdateView, BorrowRecordDeleteView,
    member_borrow_history, book_borrow_history, search_books, search_members,
)

app_name = 'library'

urlpatterns = [
    # Book URLs
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/borrow-history/', book_borrow_history, name='book_borrow_history'),
    
    # Member URLs
    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('members/create/', MemberCreateView.as_view(), name='member_create'),
    path('members/<int:pk>/update/', MemberUpdateView.as_view(), name='member_update'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member_delete'),
    path('members/<int:pk>/borrow-history/', member_borrow_history, name='member_borrow_history'),
    
    # Borrow Record URLs
    path('borrow/', BorrowRecordListView.as_view(), name='borrowrecord_list'),
    path('borrow/<int:pk>/', BorrowRecordDetailView.as_view(), name='borrowrecord_detail'),
    path('borrow/create/', BorrowRecordCreateView.as_view(), name='borrowrecord_create'),
    path('borrow/<int:pk>/update/', BorrowRecordUpdateView.as_view(), name='borrowrecord_update'),
    path('borrow/<int:pk>/delete/', BorrowRecordDeleteView.as_view(), name='borrowrecord_delete'),
    
    # Search URLs
    path('search/books/', search_books, name='search_books'),
    path('search/members/', search_members, name='search_members'),
]