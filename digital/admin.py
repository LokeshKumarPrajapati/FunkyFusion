from django.contrib import admin
from django import forms
from .models import Service, BlogPost, ContactForm, MyModel, FAQ, Testimonial, SiteSettings, News
from .models import InstagramCard, AboutUs, HomePageContent
from .models import CursorImage

from django.contrib import admin
from .models import HomePageContent

admin.site.register(InstagramCard)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['email', 'textarea', 'file']
    search_fields = ['email', 'textarea']
    list_filter = ['email']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    search_fields = ('title',)

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author')
    search_fields = ('quote', 'author')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('get_logo_preview',)
    readonly_fields = ('get_logo_preview',)

    def get_logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" style="max-width: 100px; max-height: 100px;" />'
        else:
            return 'No Image'
    get_logo_preview.allow_tags = True
    get_logo_preview.short_description = 'Logo Preview'

    def save_model(self, request, obj, form, change):
        if 'logo' in form.cleaned_data:
            obj.logo = form.cleaned_data['logo']
        super().save_model(request, obj, form, change)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'logo':
            kwargs['widget'] = forms.FileInput
        return super().formfield_for_dbfield(db_field, **kwargs)



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)



# admin.py
from django.contrib import admin
from .models import SocialMediaIcons

@admin.register(SocialMediaIcons)
class SocialMediaIconsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_heart_icon_preview', 'get_comment_icon_preview', 'get_share_icon_preview', 'get_bookmark_icon_preview')
    readonly_fields = ('get_heart_icon_preview', 'get_comment_icon_preview', 'get_share_icon_preview', 'get_bookmark_icon_preview')

    def get_heart_icon_preview(self, obj):
        return self.get_icon_preview(obj.heart_icon)

    def get_comment_icon_preview(self, obj):
        return self.get_icon_preview(obj.comment_icon)

    def get_share_icon_preview(self, obj):
        return self.get_icon_preview(obj.share_icon)

    def get_bookmark_icon_preview(self, obj):
        return self.get_icon_preview(obj.bookmark_icon)

    def get_icon_preview(self, icon):
        if icon:
            return f'<img src="{icon.url}" style="max-width: 50px; max-height: 50px;" />'
        else:
            return 'No Image'
    get_heart_icon_preview.allow_tags = True
    get_heart_icon_preview.short_description = 'Heart Icon Preview'
    get_comment_icon_preview.allow_tags = True
    get_comment_icon_preview.short_description = 'Comment Icon Preview'
    get_share_icon_preview.allow_tags = True
    get_share_icon_preview.short_description = 'Share Icon Preview'
    get_bookmark_icon_preview.allow_tags = True
    get_bookmark_icon_preview.short_description = 'Bookmark Icon Preview'




@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('header', 'subheader', 'title', 'paragraph', 'image')
    search_fields = ('header', 'subheader', 'title')


class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('header', 'subheader', 'description', 'image')
    search_fields = ('header', 'subheader')






@admin.register(CursorImage)
class CursorImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)