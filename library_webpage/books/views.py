from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)  # 5 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {'page_obj': page_obj})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')
