from django.db import models

# Модель "О себе"
class AboutMe(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фото")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "О себе"
        verbose_name_plural = "О себе"

# Модель "Руководство"
class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фото")
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководство"

# Модель "Сокурсники"
class Classmate(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фото")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сокурсник"
        verbose_name_plural = "Сокурсники"

# Модель "Отзывы"
class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name="Автор отзыва")
    content = models.TextField(verbose_name="Содержание отзыва")
    rating = models.IntegerField(verbose_name="Оценка (1-10)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    
    def __str__(self):
        return f"{self.author} - {self.rating}/10"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']  # сортировка по дате (новые сверху)


class PageContent(models.Model):
    page_name = models.CharField(max_length=100, unique=True, verbose_name="Название страницы")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ссылка на картинку")

    category = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Категория"
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.page_name
