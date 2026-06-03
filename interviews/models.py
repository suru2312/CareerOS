from django.db import models
from django.conf import settings

class Interview(models.Model):
    RESULT_CHOICES = [
        ('pending', 'Pending'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]
    MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    round_name = models.CharField(max_length=255)
    interview_date = models.DateField()
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='online')
    result = models.CharField(max_length=20, choices=RESULT_CHOICES, default='pending')
    feedback = models.TextField(blank=True)
    questions_asked = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.company_name} - "f"{self.round_name}")