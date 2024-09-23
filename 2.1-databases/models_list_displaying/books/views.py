import datetime

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.all().order_by('author')

    context = {'books': books}
    return render(request, template, context)

def book_by_date_view(request, pub_date):
    template = 'books/book_by_date.html'

    try:
        selected_date = datetime.datetime.strptime(pub_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404('Некорректный формат даты')

    book = get_object_or_404(Book, pub_date=selected_date)

    previous_book = Book.objects.filter(pub_date__lt=selected_date).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date__gt=selected_date).order_by('pub_date').first()

    context = {
        'book': book,
        'previous_book': previous_book,
        'next_book': next_book,
    }

    return render(request, template, context)