# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField
from filer.fields.image import FilerImageField


class Teaser(CMSPlugin):
    title = models.CharField(verbose_name=_("title"), max_length=64)
    teaser_text = models.TextField(verbose_name=_("text"))
    image = FilerImageField(verbose_name=_("image"))
    link_url = models.URLField(verbose_name=_("link (URL)"), max_length=255, blank=True, verify_exists=False)
    link_page = PageField(verbose_name=_("link (page)"), blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" % self.title
    
    class Meta:
        verbose_name=_("teaser")
        verbose_name_plural=_("teasers")
