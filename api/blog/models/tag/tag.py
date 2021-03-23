from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from blog.models.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/profile/[my-slug]/")
    )

    class Meta:
        db_table = 'blg_tag'

    @property
    def get_name(self) -> str:
        return '#' + self.name.title().replace(' ', '')

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
