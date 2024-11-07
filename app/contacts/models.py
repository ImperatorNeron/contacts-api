from django.db import models

from .validators import validate_phone_number


class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефону",
        validators=[validate_phone_number],
    )
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Контакти"
        verbose_name_plural = "Контакти"
