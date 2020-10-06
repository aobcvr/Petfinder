from django.db import models


class EmailAuth(models.Model):
    user = models.ForeignKey('listanimal.CustomUser',on_delete=models.PROTECT)
    key = models.CharField(max_length=199)
    time_create = models.DateTimeField(auto_now_add=True)