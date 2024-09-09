from django.db import models

class Course(models.Model):
    #name = models.CharField(max_length=200, unique=True,verbose_name="Kurs Adı", help_text="Kurs adını yazınız")
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/default_course_img.jpg")
    date = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
