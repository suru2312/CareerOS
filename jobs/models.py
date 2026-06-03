from django.db import models
from django.conf import settings


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('saved', 'Saved'),
        ('applied', 'Applied'),
        ('assessment', 'Assessment'),
        ('interview', 'Interview'),
        ('hr_round', 'HR Round'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    job_url = models.URLField(blank=True)
    application_date = models.DateField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='saved')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.position}"