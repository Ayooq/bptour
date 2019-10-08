from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField
from wagtail.core.models import Page


class HomePage(Page):
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    api_fields = [
        APIField("banner_image"),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel("banner_image")
    ]
