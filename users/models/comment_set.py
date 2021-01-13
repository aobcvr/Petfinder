from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .comment import Comment

class EmailAuthAsk(models.Model):

    comment = GenericRelation(Comment, object_id_field="object_pk")
