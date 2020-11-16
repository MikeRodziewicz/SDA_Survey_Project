from django.contrib import admin
from .models import TestModel, WisdomNote, NewsTags, NewsCategory

admin.site.register(TestModel)
admin.site.register(WisdomNote)
admin.site.register(NewsTags)
admin.site.register(NewsCategory)
