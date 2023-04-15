from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Profil Adı"), max_length=50)
    image = models.ImageField(
        ("Profil Resmi"), upload_to='Profil', max_length=200)
    password = models.CharField(("Şifre"), max_length=50, null=True)
    password_active = models.BooleanField(("Şifrele"), default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profiller"
