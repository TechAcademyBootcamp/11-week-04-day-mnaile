from django.shortcuts import render
from myapp.models import *
from django.db.models import Avg, Sum


# Create your views here.


def t1():
    books = Book.objects.all()
    print(books)
    authors = Author.objects.all()
    print(authors)
    categories = Category.objects.all()
    print(categories)

def t2():
    books = Book.objects.filter(price__lt=15)

def t3():
    authors = Author.objects.filter(date_of_birthday__year__lt=2000, date_of_birthday__year__gt=1900)

def t4():
    books = Book.objects.filter(title__icontains='a')
    categories = Category.objects.filter(title__icontains='a')

def t5():
    authors = Author.objects.filter(fullname='Daniel Defoe')

def t6():
    authors = Author.objects.exclude(nationality='British')

def t7():
    books = Book.objects.filter(author__fullname__startswith='D')

def t8():
    books = Book.objects.filter(author__gender=1)

def t9():
    books = Book.objects.filter(category__title__endswith='e')

def t10():
    books = Book.objects.get(id=3)

def t11():
    categories = Category.objects.filter()



#task 2

def task1():
    books = Book.objects.all().update(category='update')

def task2():
    books = Book.objects.filter(author__gender=2).update(price=13.8)

def task3():
    books = Book.objects.all().delete(page_count__gte=200)

def task4():
    authors = Author.objects.filter(fullname__icontains='a').order_by(date_of_birthday)

def task5():
    books = Book.objects.all().distinct()

def task6():
    new_author = Author.objects.get(id=1)
    books, created = Book.objects.get_or_create(
        author = new_author, title="Tech Academy", description="XXX", price=112, page_count=235, cover_image = "/images/1.jpeg"
        )
    if created:
        cat1 = Category.objects.get(id=2)
        cat2 = Category.objects.get(id=3)
        books.category.add(cat1,cat2)
    print(books)

def task7():
    books = Book.objects.filter(category__title='Novel').count()

def task8():
    book = Book.objects.first()
    authors = Author.objects.last()

def task9():
    book = Book.objects.order_by('id').reverse()[:3]

def task10():
    price_sum = Book.objects.aggregate(Sum('price'))
    price_avg = Book.objects.aggregate(Avg('price'))


def task12():
    book = Book.objects.filter(page_count__lt=200)
    book = Book.objects.filter(price__gt=15)
