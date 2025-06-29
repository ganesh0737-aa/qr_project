from django.db import models

class QRCode(models.Model):
    data = models.CharField(max_length=200)
    image = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.data
