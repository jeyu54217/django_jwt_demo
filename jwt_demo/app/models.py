from django.db import models


class User(models.Model):
    user_name = models.CharField(
            max_length=10,
            db_index=True
        )
    user_password = models.CharField(
            max_length=10,
            db_index=True
        )

