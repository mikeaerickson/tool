# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Survey
from .models import Profile
from .models import Design


admin.site.register(Survey)
admin.site.register(Profile)
admin.site.register(Design)

# Register your models here.
