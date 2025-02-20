from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


#Django ORM
# O - Object 
# R - Relation
# M - Mapper
#The Django ORM tool helps with the relation of classes in Python with the tables in the Database

class Posts(models.Model):
  content = models.CharField(max_length=300, null=True)

  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Post by: {self.posted_by.username}"

  

#Advanced model relatioships