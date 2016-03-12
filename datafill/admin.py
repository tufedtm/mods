from django.contrib import admin
from . import models


class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'updated']


class MagazineAdmin(ReadOnlyFields):
    list_display = ['title_display']

    def title_display(self, obj):
        return '%s %s' % (obj.get_title_display(), obj.number)


class DemoImgInline(admin.TabularInline):
    model = models.DemoImg
    extra = 1
    show_change_link = True


class DemoAdmin(ReadOnlyFields):
    inlines = [DemoImgInline]


admin.site.register(models.Magazine, MagazineAdmin)
admin.site.register(models.Game, ReadOnlyFields)
admin.site.register(models.Patch, ReadOnlyFields)
admin.site.register(models.Demo, DemoAdmin)
admin.site.register(models.DemoImg, ReadOnlyFields)
admin.site.register(models.ThemeDVD, ReadOnlyFields)
