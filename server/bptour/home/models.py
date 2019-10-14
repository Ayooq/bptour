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

    address = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name='адрес агентства',
    )
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=False,
        verbose_name='электронная почта',
    )

    max_count = 1

    api_fields = [
        APIField('related_links'),
    ]

    tours_panels = [
        MultiFieldPanel(
            [InlinePanel('carousel', min_num=2, max_num=5,
                         label='слайд для карусели')],
            heading='основные направления',
        ),
        MultiFieldPanel(
            [InlinePanel('gallery', min_num=2, max_num=12,
                         label='карточку для галереи')],
            heading='дополнительные направления',
        ),
    ]

    contacts_panels = [
        FieldPanel('address'),
        MultiFieldPanel(
            [InlinePanel('phone_numbers', label='номер телефона')],
            heading='номера стационарных телефонов',
        ),
        MultiFieldPanel(
            [InlinePanel('phone_numbers', label='номер телефона')],
            heading='номера мобильных телефонов',
        ),
        MultiFieldPanel(
            [InlinePanel('related_links', label='ссылку')],
            heading='ссылки на соцсети',
        ),
        FieldPanel('email'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(tours_panels, heading='туры'),
        ObjectList(contacts_panels, heading='контакты'),
        ObjectList(Page.promote_panels, heading='продвижение'),
        ObjectList(Page.settings_panels, heading='настройки',
                   classname="settings"),
    ])

    class Meta:
        verbose_name = 'домашняя страница'
        verbose_name_plural = 'домашние страницы'


class HomePageCarousel(Orderable):
    """Карусель на домашней странице."""

    page = ParentalKey(HomePage, related_name='carousel')

    slide_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="изображение",
    )
    slide_caption = models.CharField(
        max_length=80,
        blank=True,
        verbose_name='подпись',
    )
    full_description = RichTextField(
        max_length=400,
        blank=True,
        features=['bold', 'ol', 'ul', 'hr'],
        verbose_name='подробное описание',
    )

    panels = [
        ImageChooserPanel('slide_image'),
        FieldPanel('slide_caption'),
        FieldPanel('full_description'),
    ]


class HomePageGallery(Orderable):
    """Галерея на домашней странице."""

    page = ParentalKey(HomePage, related_name='gallery')

    gallery_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="изображение",
    )
    short_description = RichTextField(
        max_length=255,
        blank=True,
        features=['bold', 'ol', 'ul', 'hr'],
        verbose_name='краткое описание',
    )

    panels = [
        ImageChooserPanel('gallery_image'),
        FieldPanel('short_description'),
    ]


class HomePagePhone(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name='phone_numbers')

    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=False,
        verbose_name='номер телефона',
    )


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
