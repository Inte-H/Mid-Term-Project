from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    post_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    # author 나중에

    def __str__(self):
        return f'{self.title}'