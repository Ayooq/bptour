from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    PageChooserPanel,
    StreamFieldPanel,
    TabbedInterface,
)
from wagtail.api import APIField
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """Домашняя страница."""

    max_count = 1

    api_fields = [
        APIField('related_links'),
    ]

    tours_panels = [
        MultiFieldPanel(
            [InlinePanel('carousel_images', min_num=2, max_num=5,
                         label='изображение')],
            heading='основные направления',
        ),
    ]

    contacts_panels = [
        MultiFieldPanel(
            [InlinePanel('related_links', label='ссылку')],
            heading='ссылки на соцсети',
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(tours_panels, heading='Туры'),
        ObjectList(contacts_panels, heading='Контакты'),
        ObjectList(Page.promote_panels, heading='Продвижение'),
        ObjectList(Page.settings_panels, heading='Настройки',
                   classname="settings"),
    ])

    class Meta:
        verbose_name = 'домашняя страница'
        verbose_name_plural = 'домашние страницы'


class HomePageCarouselImages(Orderable):
    """От двух до пяти изображений для карусели домашней страницы."""

    page = ParentalKey(HomePage, related_name='carousel_images')
    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="изображение",
    )

    panels = [ImageChooserPanel('carousel_image')]


class HomePageRelatedLink(Orderable):
    """Ссылка на внешний ресурс."""

    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name='related_links')
    caption = models.CharField(
        max_length=255,
        verbose_name='подпись',
    )
    url = models.URLField()

    panels = [
        FieldPanel('caption'),
        FieldPanel('url'),
    ]
