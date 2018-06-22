from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
                 'num_visits' : num_visits},
    )

class BookListView(generic.ListView):
    model = Book
    template_name = "book_list.html"
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book_detail.html"

class AuthorListView(generic.ListView):
    model = Author
    template_name = "author_list.html"
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "author_detail.html"
    paginate_by = 2

    # def get_context_data(self,**kwargs):
    #      # В первую очередь получаем базовую реализацию контекста
    #     context = super().get_context_data(**kwargs) # AuthorDetailView, self
    #     # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
    #     context['authors_books'] = model.author_set()  '12345' #Book.objects.filter(author=self)
    #     return context               