from django.db import models
from django.urls import reverse
# Create your models here.


class Device(models.Model):
    # Fields
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()

    # Metadata
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('deviceDetails', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

    def getDigitalGetUrl(self):
        return 'digital/' + str(self.id)