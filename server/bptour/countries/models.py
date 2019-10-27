from django.db import models
from django.utils.text import slugify
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.search import index


class CountriesIndexPage(Page):
    """Страница указателя стран."""

    max_count = 1

    subpage_types = ['CountryDetailsPage']

    # api_fields = [
    #     APIField('countries'),
    # ]

    def get_context(self, request):
        context = super().get_context(request)
        context['countries'] = CountryDetailsPage.objects.live().public()

        return context

    class Meta:
        verbose_name = 'Список стран'


class CountryDetailsPage(Page):
    """Страница детальной информации о стране."""

    country_name = models.CharField(
        max_length=80,
        unique=True,
        verbose_name='название страны',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='изображение',
    )
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

    parent_page_types = ['CountriesIndexPage']
    subpage_types = []

    api_fields = [
        APIField('country_name'),
        APIField('image'),
        APIField('description'),
        APIField('additional'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('additional'),
    ]

    content_panels = [
        FieldPanel('country_name', classname='title'),
        ImageChooserPanel('image'),
        FieldPanel('description', classname="full"),
        FieldPanel('additional', classname="full"),
    ]

    def clean(self):
            """Переписать значение заголовка перед сохранением."""
            super().clean()
            self.title = self.country_name
            self.slug = slugify(self.title)
            self.seo_title = f'{self.title}. Детальная информация.'

    class Meta:
        verbose_name = 'Детальная информация о стране'
