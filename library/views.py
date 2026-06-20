from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Member, BorrowRecord
from .forms import BookForm, MemberForm, BorrowRecordForm

# ============ BOOK VIEWS ============

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('library:book_list')


# ============ MEMBER VIEWS ============

class MemberListView(ListView):
    model = Member
    template_name = 'library/member_list.html'
    context_object_name = 'members'
    paginate_by = 10


class MemberDetailView(DetailView):
    model = Member
    template_name = 'library/member_detail.html'
    context_object_name = 'member'


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'library/member_form.html'
    success_url = reverse_lazy('library:member_list')


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'library/member_form.html'
    success_url = reverse_lazy('library:member_list')


class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'library/member_confirm_delete.html'
    success_url = reverse_lazy('library:member_list')


# ============ BORROW RECORD VIEWS ============

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'library/borrowrecord_list.html'
    context_object_name = 'records'
    paginate_by = 10


class BorrowRecordDetailView(DetailView):
    model = BorrowRecord
    template_name = 'library/borrowrecord_detail.html'
    context_object_name = 'record'


class BorrowRecordCreateView(CreateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'library/borrowrecord_form.html'
    success_url = reverse_lazy('library:borrowrecord_list')


class BorrowRecordUpdateView(UpdateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'library/borrowrecord_form.html'
    success_url = reverse_lazy('library:borrowrecord_list')


class BorrowRecordDeleteView(DeleteView):
    model = BorrowRecord
    template_name = 'library/borrowrecord_confirm_delete.html'
    success_url = reverse_lazy('library:borrowrecord_list')

# ============ RELATIONSHIP VIEWS ============

def member_borrow_history(request, pk):
    """Show all books borrowed by a specific member"""
    member = get_object_or_404(Member, pk=pk)
    borrow_records = member.borrow_records.all()
    
    context = {
        'member': member,
        'borrow_records': borrow_records,
    }
    return render(request, 'library/member_borrow_history.html', context)


def book_borrow_history(request, pk):
    """Show all members who borrowed a specific book"""
    book = get_object_or_404(Book, pk=pk)
    borrow_records = book.borrow_records.all()
    
    context = {
        'book': book,
        'borrow_records': borrow_records,
    }
    return render(request, 'library/book_borrow_history.html', context)

# ============ SEARCH VIEWS ============

def search_books(request):
    """Search books by title or author"""
    query = request.GET.get('q', '')
    books = Book.objects.all()
    
    if query:
        books = books.filter(
            title__icontains=query
        ) | books.filter(
            author__icontains=query
        )
    
    context = {
        'books': books,
        'query': query,
        'search_type': 'Books',
    }
    return render(request, 'library/search_results.html', context)


def search_members(request):
    """Search members by name or email"""
    query = request.GET.get('q', '')
    members = Member.objects.all()
    
    if query:
        members = members.filter(
            first_name__icontains=query
        ) | members.filter(
            last_name__icontains=query
        ) | members.filter(
            email__icontains=query
        )
    
    context = {
        'members': members,
        'query': query,
        'search_type': 'Members',
    }
    return render(request, 'library/search_results.html', context)