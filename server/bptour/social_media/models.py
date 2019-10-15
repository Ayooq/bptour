from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting(icon='link')
class SocialMediaSettings(BaseSetting):
    """Пункт меню в настройках для соцсетей."""

    whatsapp = models.URLField(
        null=True,
        blank=True,
        verbose_name="what's App",
    )
    instagram = models.URLField(null=True, blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('whatsapp'),
            FieldPanel('instagram'),
        ], heading='ссылки на соцсети')
    ]

    class Meta:
        verbose_name = 'соцсети'
