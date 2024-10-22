from django.db import models

# Create your models here.
from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Waypoint(models.Model):
    route = models.ForeignKey(Route, related_name='waypoints', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
