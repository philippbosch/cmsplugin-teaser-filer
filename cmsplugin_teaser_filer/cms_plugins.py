# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import Teaser


class TeaserPlugin(CMSPluginBase):
    model = Teaser
    name = _("teaser")
    render_template = "plugins/teaser/teaser.html"
    text_enabled = False
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        context.update({
            'teaser': instance,
            'placeholder': placeholder
        })
        return context 

plugin_pool.register_plugin(TeaserPlugin)
