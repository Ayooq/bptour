from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """Домашняя страница."""

    address = models.CharField(
        max_length=254,
        null=True,
        verbose_name='адрес агентства',
    )
    email = models.EmailField(
        max_length=80,
        null=True,
        verbose_name='электронная почта',
    )

    max_count = 1

    api_fields = [
        APIField('carousel'),
        APIField('gallery'),
        APIField('address'),
        APIField('landline_phones'),
        APIField('mobile_phones'),
        APIField('social_links'),
        APIField('email'),
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
        MultiFieldPanel([
            InlinePanel('landline_phones', min_num=1,
                        max_num=3, label='стационарный телефон'),
            InlinePanel('mobile_phones', min_num=1,
                        max_num=3, label='мобильный телефон'),
        ], heading='номера телефонов'),
        MultiFieldPanel(
            [InlinePanel('social_links', label='ссылку')],
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

    def clean(self):
            """Переписать значение заголовка перед сохранением."""
            super().clean()
            self.title = 'Главная'

    class Meta:
        verbose_name = 'домашняя страница'


class CarouselSlide(Orderable):
    """Слайд для карусели."""

    page = ParentalKey(HomePage, related_name='carousel')

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="изображение",
    )
    caption = models.CharField(
        max_length=80,
        verbose_name='подпись',
    )
    full_description = RichTextField(
        max_length=511,
        blank=True,
        features=['bold', 'ol', 'ul', 'hr'],
        verbose_name='подробное описание',
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('full_description'),
    ]


class GalleryCard(Orderable):
    """Карточка для галереи."""

    page = ParentalKey(HomePage, related_name='gallery')

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="изображение",
    )
    short_description = RichTextField(
        max_length=254,
        blank=True,
        features=['bold', 'ol', 'ul', 'hr'],
        verbose_name='краткое описание',
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('short_description'),
    ]


class LandlinePhone(Orderable):
    """Номер стационарного телефона."""

    page = ParentalKey(HomePage, related_name='landline_phones')

    phone_number = models.CharField(
        max_length=20,
        null=True,
        unique=True,
        verbose_name='стационарный телефон',
    )

    panels = [FieldPanel('phone_number')]


class MobilePhone(Orderable):
    """Номер мобильного телефона."""

    page = ParentalKey(HomePage, related_name='mobile_phones')

    phone_number = models.CharField(
        max_length=20,
        null=True,
        unique=True,
        verbose_name='мобильный телефон',
    )

    panels = [FieldPanel('phone_number')]


class SocialLink(Orderable):
    """Ссылка на соцсеть."""

    page = ParentalKey(HomePage, related_name='social_links')

    caption = models.CharField(
        max_length=80,
        verbose_name='подпись',
    )
    url = models.URLField(
        null=True,
        blank=True,
        unique=True,
        help_text='Адрес',
    )

    panels = [
        FieldPanel('caption'),
        FieldPanel('url'),
    ]
