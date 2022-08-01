from django.db import models


class Comment_pig(models.Model):
    comment = models.TextField(verbose_name='Комментарии', max_length=255)

    def __str__(self):
        return self.comment


class Comment_kenguru(models.Model):
    comment = models.TextField(verbose_name='Комментарии', max_length=255)

    def __str__(self):
        return self.comment


