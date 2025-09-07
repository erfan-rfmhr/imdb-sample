from django.db import models


class Movie(models.Model):
    # == Fields ==
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField()
    media = models.FileField(upload_to='movies/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # == Relations ==
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
