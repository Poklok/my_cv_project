from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    img = models.ImageField(upload_to='img/avatar', default=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    author = models.ForeignKey(Developer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=450)
    created = models.DateTimeField(auto_now_add=True)
    img_post = models.ImageField(upload_to='img/post', default=True)

    def __str__(self):
        return f'Пост {self.author}'

    def get_absolut_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Project(models.Model):
    COMPLEXITY_CHOICES = [
        ('Easy', 'easy'),
        ('Normal', 'normal'),
        ('Hard', 'hard'),
    ]
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project_url = models.CharField(max_length=150)
    about_project = models.TextField(max_length=400)
    complexity = models.CharField(max_length=6, choices=COMPLEXITY_CHOICES, blank=True)
    img_project = models.ImageField(upload_to='img/project', default=True)
    skills = models.TextField(max_length=200)

    def __str__(self):
        return self.about_project
    # def get_absolut_url(self):
    #     return reverse('post_detail', kwargs={'pk': self.pk})


class CommentForPost(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author_comment = models.CharField(max_length=50)
    content_comment = models.TextField(max_length=200)
    created_comment = models.DateTimeField(auto_now_add=True)
    status_comment = models.BooleanField(default=True)

    def __str__(self):
        return f'Комментарий от {self.author_comment} для: - {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_comment',)
