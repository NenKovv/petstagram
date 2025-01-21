# pets/models.py

from django.db import models
from django.template.defaultfilters import slugify

from petstagram.core.model_mixins import StrFromFieldsMixin

# Create your models here.

'''
The fields Name and Pet Photo are required:
•	Name - it should consist of a maximum of 30 characters.
•	Personal Pet Photo - the user can link a picture using a URL
The field date of birth is optional:
•	Date of Birth - pet's day, month, and year of birth

'''



class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super().save(*args, **kwargs)

    # Without 'if'  the slug would be changed
    # /pets/4-stamat
    # Rename stamat to stamata
    # /pets/4-stamata, /pets/4-stamat does not work


    # I will replace it with mixin
    # def __str__(self):
    #   return f'Id={self.id}; Name={self.name}'