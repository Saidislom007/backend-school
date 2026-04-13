from django.db import models
from django.utils import timezone

# 1. Blog Post
class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Ta\'lim', 'Ta\'lim'),
        ('Maslahatlar', 'Maslahatlar'),
        ('Sport', 'Sport'),
        ('Tarbiya', 'Tarbiya'),
        ('Olimpiadalar', 'Olimpiadalar'),
        ('Yangiliklar', 'Yangiliklar'),
    ]
    
    title = models.CharField(max_length=300)
    excerpt = models.TextField()
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=200, default="Erkinov Ziyodullo")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    comments_count = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']


# 2. Teacher
class Teacher(models.Model):
    CATEGORY_CHOICES = [
        ('Oliy toifali', 'Oliy toifali'),
        ('1-toifali', '1-toifali'),
    ]
    
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    experience = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    qualification = models.CharField(max_length=200, blank=True)
    students_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


# 3. Gallery Photo
class GalleryPhoto(models.Model):
    CATEGORY_CHOICES = [
        ('building', 'Maktab binosi'),
        ('classes', 'Dars jarayoni'),
        ('events', 'Tadbirlar'),
        ('sports', 'Sport'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='building')
    date = models.DateField(default=timezone.now)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


# 4. Achievement
class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('science', 'Fan olimpiadalari'),
        ('sports', 'Sport musobaqalari'),
        ('contests', 'Tanlovlar'),
    ]
    LEVEL_CHOICES = [
        ('Maktab', 'Maktab'),
        ('Shahar', 'Shahar'),
        ('Viloyat', 'Viloyat'),
        ('Respublika', 'Respublika'),
        ('Xalqaro', 'Xalqaro'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=300)
    award = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    student = models.CharField(max_length=200, blank=True)
    team = models.CharField(max_length=200, blank=True)
    winner = models.CharField(max_length=200, blank=True)
    medal = models.CharField(max_length=50, blank=True)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default='Maktab')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.award} ({self.year})"


# 5. Library Item
class LibraryItem(models.Model):
    TYPE_CHOICES = [
        ('ebook', 'Elektron kitob'),
        ('textbook', 'Rasmiy darslik'),
        ('guide', 'O\'quv qo\'llanma'),
    ]
    
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    class_level = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50)
    format = models.CharField(max_length=20, default='PDF')
    file = models.FileField(upload_to='library/', blank=True, null=True)
    downloads = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    year = models.CharField(max_length=4, blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title