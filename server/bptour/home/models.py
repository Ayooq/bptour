from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.api import APIField
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePageCarouselImages(Orderable):
    """От двух до пяти изображений для карусели домашней страницы."""

    page = ParentalKey('HomePage', related_name='carousel_images')
    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [ImageChooserPanel('carousel_image')]


class HomePageRelatedLink(Orderable):
    """Ссылка на внешний ресурс."""

    page = ParentalKey('HomePage', on_delete=models.CASCADE,
                       related_name='related_links')
    caption = models.CharField(
        verbose_name='подпись',
        max_length=255,
    )
    url = models.URLField()

    panels = [
        FieldPanel('caption'),
        FieldPanel('url'),
    ]


class HomePage(Page):
    """Домашняя страница."""

    max_count = 1

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    api_fields = [
        APIField('banner_image'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner_image'),
        MultiFieldPanel(
            [InlinePanel('carousel_images', min_num=2, max_num=5,
                         label='Изображение')],
            heading='Основные направления',
        ),
        MultiFieldPanel(
            [InlinePanel('related_links', label='Ссылка')],
            heading='Ссылки на соцсети',
        ),
    ]

    class Meta:
        verbose_name = 'Домашняя страница'
        verbose_name_plural = 'Домашние страницы'
