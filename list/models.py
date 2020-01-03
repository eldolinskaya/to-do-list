from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class List(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name = "Клиент",
        null = True,
        blank = True,
        on_delete = models.PROTECT)
    name = models.CharField(max_length=200, verbose_name="Наименование")
    done = models.BooleanField(default=True, verbose_name="Выполнено")
    
    def get_absolute_url(self):
        return f'/list/{self.pk}/'

    def __str__(self):
        return self.name

