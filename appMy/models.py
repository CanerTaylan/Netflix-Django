from django.db import models


class Series(models.Model):
    title = models.CharField(("Dizi İsim"), max_length=50)
    image = models.ImageField(
        ("Dizi Resim"), upload_to='Series', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dizi"
        verbose_name_plural = "Diziler"


class Films(models.Model):
    title = models.CharField(("Film İsim"), max_length=50)
    image = models.ImageField(
        ("Film Resim"), upload_to='Films', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmler"

class Categories(models.Model):
    title = models.CharField(("Kategori"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


class Contents(models.Model):
    Categories = models.ForeignKey(Categories, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title= models.CharField(("isim"), max_length=150)
    image = models.ImageField(("Resim"), upload_to='Content', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "İçerik"
        verbose_name_plural = "İçerikler"