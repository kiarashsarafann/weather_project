from django.db import models


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=128)
    company = models.CharField(max_length=80, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'