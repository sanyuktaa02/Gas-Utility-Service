from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
    ]
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    details = models.TextField()
    file_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service_type}"
