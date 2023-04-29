from django.db import models


class Post(models.Model):
    SECTION_CHOICES = [
        ('Раздел 1', 'Раздел 1'),
        ('Раздел 2', 'Раздел 2'),
    ]
    title = models.CharField(max_length=450)  # заголовок поста
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, null=True)

    def __str__(self):  # Метод
        return self.title
