from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect

from p_library.models import Book

# Create your views here.

def books_list():
    books = Book.objects.all()
    qs_json = serializers.serialize('json', books)
    return HttpResponse(qs_json, content_type='application/json')

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "loop": range(1, 101),
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publisher_list(request):
    return render(request, 'publishers.html', {
        'publishers': Book.objects.select_related('publisher').order_by('publisher'),
    },)