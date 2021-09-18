from django.db import models


class Person(models.Model):
    person_name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.person_name