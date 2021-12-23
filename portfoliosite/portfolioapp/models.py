from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=150)
    title_of_card = models.CharField(max_length=100)
    body = models.TextField()
    title_image = models.ImageField(upload_to='work_title_image/',
                                    null=True,
                                    blank=True)
    upper_image = models.ImageField(upload_to='work_title_image/',
                                    null=True,
                                    blank=True)
    first_body_image = models.ImageField(upload_to='work_body_image/',
                                         null=True,
                                         blank=True)
    second_body_image = models.ImageField(upload_to='work_body_image/',
                                          null=True,
                                          blank=True)
    third_body_image = models.ImageField(upload_to='work_body_image/',
                                         null=True,
                                         blank=True)
    body_title = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="The date and time the work was added.")

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="The date and time when the message was sent")

    def __str__(self):
        return self.subject


class Tag(models.Model):
    pass


class About(models.Model):
    title_1 = models.CharField(max_length=200)
    title_2 = models.CharField(max_length=200)
    title_3 = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_me/',
                              null=True,
                              blank=True)
    body_1 = models.TextField()
    body_2 = models.TextField()
    body_3 = models.TextField()

    def __str__(self):
        return self.title_1