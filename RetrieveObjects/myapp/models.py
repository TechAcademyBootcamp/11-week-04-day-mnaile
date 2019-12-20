from django.db import models

# Create your models here.

class Author(models.Model):
    #relation


    #information
    fullname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/image')
    gender = models.IntegerField(choices=((1, 'qadin'), (2, 'kisi')))
    date_of_birthday = models.DateField()
    nationality = models.CharField(max_length=255)
    info = models.TextField()

    #moderator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fullname} {self.date_of_birthday}"

class Book(models.Model):
    #relation
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    #information
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    page_count = models.IntegerField()
    cover_image = models.ImageField(upload_to='media/image')

    #moderator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.author} {self.price} {self.page_count}"

class Category(models.Model):
    #relation
    
    #information
    title = models.CharField(max_length=255)

    #moderator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# class Relation(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)

