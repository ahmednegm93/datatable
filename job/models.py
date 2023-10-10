from django.db import models

job_types=((
'full time','full time'
),(
    'part time','part time'
)
           )


# Create your models here.
class job(models.Model):
    title=models.CharField(max_length=100)
    job_type=models.CharField(choices=job_types,max_length=50)
    describtion=models.TextField(max_length=100)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    
    class Meta:
            verbose_name_plural = "jobs"
    def __str__(self):
        return self.title
   
class category(models.Model):
    name=models.CharField(max_length=25)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name