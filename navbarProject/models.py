from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pages(models.Model):
    page_name = models.CharField('page name', max_length=30)
    page_image = models.ImageField(null=True, blank=True, upload_to="images/")
    auth_users = models.ManyToManyField(User, blank=True)
    web = models.URLField('website page', blank=True, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.web = "http://127.0.0.1:8000/" + self.page_name

    def save(self, *args, **kwargs):
        if self.web != "http://127.0.0.1:8000/" + self.page_name:
            self.web = "http://127.0.0.1:8000/" + self.page_name
        super().save(*args, **kwargs)
