from django.db import models

class MyModel(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        permissions = (
            ('view_mymodel', 'View mymodel'),
        )
