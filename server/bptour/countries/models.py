from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.search import index


class CountriesPage(Page):
    page = PageChooserPanel('countries.CountryDetailsPage')

    subpage_types = ['countries.CountryDetailsPage']


class CountryDetailsPage(Page):
    country_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='изображение',
    )
    country_name = models.CharField(
        verbose_name='название страны', max_length=80)
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

    parent_page_types = ['countries.CountriesPage']

    search_fields = Page.search_fields + [
        index.SearchField('country_name'),
        index.SearchField('description'),
        index.SearchField('additional'),
    ]

    content_panels = [
        ImageChooserPanel('country_image'),
        FieldPanel('country_name'),
        FieldPanel('description', classname="full"),
        FieldPanel('additional', classname="full"),
    ]

    class Meta:
        verbose_name = 'Детальная информация о стране'
