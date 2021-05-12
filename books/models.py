import uuid 

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("book_detail", kwargs={"pk": self.pk})
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.review
    
