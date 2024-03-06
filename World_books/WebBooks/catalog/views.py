from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instaces_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html', context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instaces_available': num_instaces_available,
                                                  'num_authors': num_authors,
                                                  'num_visits': num_visits,
                                                  },)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')
                