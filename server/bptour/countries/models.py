from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.search import index


class DetailPage(Page):
    country = models.CharField(verbose_name='заголовок', max_length=80)
    subtitle = models.CharField(verbose_name='подзаголовок', max_length=250)
    description = RichTextField(blank=True)
    additional = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('subtitle'),
        index.SearchField('description'),
        index.SearchField('additional'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('description', classname="full"),
        FieldPanel('additional', classname="full"),
    ]
