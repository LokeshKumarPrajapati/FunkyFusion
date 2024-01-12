from django.db import models

class ContactForm(models.Model):
    email = models.EmailField()
    textarea = models.TextField()
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.email

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icons/')
    description = models.TextField()

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonial_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.quote[:50]}..."

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='site_logo/', blank=True, null=True)

    def __str__(self):
        return f"Site Settings - {self.pk}"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TemplateInfo(models.Model):
    subheader = models.CharField(max_length=255)
    header = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subheader} - {self.header}"

class Image(models.Model):
    file = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image - {self.pk}"

class InstaHighlight(models.Model):
    template_info = models.ForeignKey(TemplateInfo, on_delete=models.CASCADE)
    bg_images = models.ManyToManyField(Image, related_name='insta_highlight_bg_images')
    profile_image = models.ImageField(upload_to='images/')
    user_name = models.CharField(max_length=255)
    user_role = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    message = models.TextField()
    user_image = models.ImageField(upload_to='images/')
    message_tags = models.ManyToManyField(Tag, related_name='insta_highlights_tags', blank=True)

    def __str__(self):
        return f"{self.template_info.subheader} - {self.template_info.header}"

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class InstagramCard(models.Model):
    bg_image1 = models.ImageField(upload_to='card_backgrounds/')
    bg_image2 = models.ImageField(upload_to='card_backgrounds/')
    bg_image3 = models.ImageField(upload_to='card_backgrounds/')
    profile_image = models.ImageField(upload_to='profile_images/')
    user_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    message = models.TextField()

    def __str__(self):
        return self.user_name

class SocialMediaIcons(models.Model):
    heart_icon = models.ImageField(upload_to='social_icons/')
    comment_icon = models.ImageField(upload_to='social_icons/')
    share_icon = models.ImageField(upload_to='social_icons/')
    bookmark_icon = models.ImageField(upload_to='social_icons/')

    def __str__(self):
        return "Social Media Icons"

class AboutUs(models.Model):
    header = models.CharField(max_length=255)
    subheader = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='about_us_images/', blank=True, null=True)

    def __str__(self):
        return f"About Us - {self.header} - {self.subheader}"

class HomePageContent(models.Model):
    header = models.CharField(max_length=200)
    subheader = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='template_images/')

    def __str__(self):
        return self.header

class DynamicImage(models.Model):
    image = models.ImageField(upload_to='dynamic_images/', blank=True, null=True)

    def __str__(self):
        return f"Dynamic Image - {self.pk}"




class CursorImage(models.Model):
    image = models.ImageField(upload_to='cursor_images/')

    def __str__(self):
        return f"Cursor Image {self.id}"