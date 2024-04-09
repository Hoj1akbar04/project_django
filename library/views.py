from django.shortcuts import render
from django.views import View
from .models import Books
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            books = Books.objects.all()
            context = {
                'books': books
            }
            return render(request, 'librarypage.html', context)

        else:
            books = Books.objects.filter(name__icontains=search)
            if not books:
                return render(request, 'not_found.html')
            else:
                context = {
                    'books': books,
                    'search': search
                }
                return render(request, 'librarypage.html', context)


class BookDetailView(View):
    def get(self, request, id):
        book = Books.objects.get(id=id)

        return render(request, 'books.html', {'book': book})