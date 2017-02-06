from django.db import models

# Create your models here.
class Header(models.Model):
    class Meta:
        db_table = "header"

    header_title = models.CharField(max_length = 200)
