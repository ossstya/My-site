from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    title_image = models.ImageField()
    first_body_image = models.ImageField()
    second_body_image = models.ImageField()
    third_body_image = models.ImageField()
    body_title = models.TextField()


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


class Tag(models.Model):
    pass