from django.db import models
from django.utils.text import slugify

import string
import random


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.TextField(null=False)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(verbose_name='slug',
                            allow_unicode=True, unique=False)


def _random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    generator = ''.join(random.choice(chars) for _ in range(size))
    print("!!!!", generator)
    return generator


def _unique_slug_generator(self, new_slug=None):
    print("!!_unique_slug_generator :", self.name, f"[{new_slug}]")
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(self.name)
    Klass = self.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = f"{slug}-{self._random_string_generator(size=4)}"
        return self._unique_slug_generator(self, new_slug=new_slug)

    return slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
