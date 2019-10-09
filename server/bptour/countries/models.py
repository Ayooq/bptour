from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.search import index


class CountryDetailPage(Page):
    country = models.CharField(verbose_name='страна', max_length=80)
    description = RichTextField(
        blank=True,
        features=['bold', 'ol', 'ul', 'hr'],
        verbose_name='описание',
    )
    additional = RichTextField(
        blank=True,
        features=['bold', 'ol', 'ul', 'hr'],
        verbose_name='дополнительная информация',
    )

    search_fields = Page.search_fields + [
        index.SearchField('country'),
        index.SearchField('description'),
        index.SearchField('additional'),
    ]

    content_panels = [
        FieldPanel('country'),
        FieldPanel('description', classname="full"),
        FieldPanel('additional', classname="full"),
    ]

    class Meta:
        verbose_name = 'Детальная информация о стране'
