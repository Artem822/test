from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter book genre's", verbose_name="Book's genre")

    def __str__(self):
        return self.name
    

class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Enter book's language", verbose_name="Book's language")

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Enter author first name", verbose_name="Author first name")
    last_name = models.CharField(max_length=100, help_text="Enter author last name", verbose_name="Author last name")
    date_of_birth = models.DateField(help_text="Enter birth date", verbose_name="Date of birth", null=True, blank=True)
    date_of_death = models.DateField(help_text="Enter death date", verbose_name="Date of death", null=True, blank=True)

    def __str__(self) -> str:
        return self.last_name
    
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Enter book's name", verbose_name="Book's name")
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, help_text="Choose genre for book", verbose_name="Book's genre", null=True)
    language = models.ForeignKey("Language", on_delete=models.CASCADE, help_text="Choose language for book", verbose_name="Book's language", null=True)
    author = models.ManyToManyField("Author", help_text="Choose book's author", verbose_name="Book's author")
    summary = models.TextField(max_length=1000, help_text="Enter summary for book", verbose_name="Book's summary")
    isbn = models.CharField(max_length=13, help_text="it's should to consist of 13 charcaters", verbose_name="Book's ISBN")

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])
    display_author.short_description = 'Authors'
    
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Enter book's status", verbose_name="Book's status")

    def __str__(self) -> str:
        return self.name
    
class BookInstance(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, help_text="Enter book's inventory number", verbose_name="Inventory number")
    imprint = models.CharField(max_length=200, help_text="Enter publisher and year of issue", verbose_name="Publisher")
    status = models.ForeignKey("Status", on_delete=models.CASCADE, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Client', help_text="Select the client's books")

    def __str__(self) -> str:
        return f'{self.inv_nom} {self.book} {self.status}'
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        
        return False