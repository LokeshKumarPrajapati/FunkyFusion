from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    BlogPost, ContactForm, FAQ, MyModel, Service, Testimonial, SiteSettings, TemplateInfo, News,
    InstagramCard, SocialMediaIcons, AboutUs, HomePageContent, DynamicImage
)
from .forms import ContactForm
from .forms import ContactFormModel
from .models import CursorImage

def my_view(request):
    # Retrieve the cursor image from the database (you might want to filter based on your requirements)
    cursor_image = CursorImage.objects.first()

    return render(request, 'my_template.html', {'cursor_image': cursor_image})


def home_page(request):
    content = HomePageContent.objects.first()
    return render(request, 'base.html', {'content': content})

def instagram_card(request):
    card_data = InstagramCard.objects.first()

    if not card_data:
        return render(request, 'no_instagram_card.html')

    return render(request, 'base.html', {'card_data': card_data})

def base_view(request):
    blog_posts = BlogPost.objects.all()
    contact_forms = ContactForm.objects.all()
    faqs = FAQ.objects.all()
    my_models = MyModel.objects.all()
    services_list = Service.objects.all()
    testimonials_list = Testimonial.objects.all()
    social_media_icons = SocialMediaIcons.objects.first()
    about_us_data = AboutUs.objects.first()
    template_info = TemplateInfo.objects.first()
    site_settings = SiteSettings.objects.first()
    news_list = News.objects.all()

    dynamic_image = DynamicImage.objects.first()

    return render(request, 'base.html', {
        'blog_posts': blog_posts,
        'contact_forms': contact_forms,
        'faqs': faqs,
        'my_models': my_models,
        'services': services_list,
        'testimonials': testimonials_list,
        'site_settings': site_settings,
        'template_info': template_info,
        'news_list': news_list,
        'social_media_icons': social_media_icons,
        'about_us_data': about_us_data,
        'template_info': template_info,
        'dynamic_image': dynamic_image,
    })

def about_us(request):
    about_us_data = AboutUs.objects.first()
    return render(request, 'about_us.html', {'about_us_data': about_us_data})

def home(request):
    blog_posts = BlogPost.objects.all()
    contact_forms = ContactForm.objects.all()
    faqs = FAQ.objects.all()
    my_models = MyModel.objects.all()
    services_list = Service.objects.all()
    testimonials_list = Testimonial.objects.all()
    social_media_icons = SocialMediaIcons.objects.first()
    template_info = TemplateInfo.objects.first()
    site_settings = SiteSettings.objects.first()
    news_list = News.objects.all()
    card_data = InstagramCard.objects.first()

    dynamic_image = DynamicImage.objects.first()

    return render(request, 'base.html', {
        'blog_posts': blog_posts,
        'contact_forms': contact_forms,
        'faqs': faqs,
        'my_models': my_models,
        'services': services_list,
        'testimonials': testimonials_list,
        'site_settings': site_settings,
        'template_info': template_info,
        'news_list': news_list,
        'card_data': card_data,
        'social_media_icons': social_media_icons,
        'dynamic_image': dynamic_image,
    })

def contact_form(request):
    if request.method == 'POST':
        form = ContactFormModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact_form')  # Redirect to the same page
    else:
        form = ContactFormModel()

    return render(request, 'base.html', {'form': form})



def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = ContactForm(instance=post)
    return render(request, 'blog/edit_blog_post.html', {'form': form, 'post': post})

def success_page(request):
    return render(request, 'success_page.html')

def services(request):
    services_list = Service.objects.all()
    testimonials_list = Testimonial.objects.all()
    return render(request, 'base.html', {'services': services_list, 'testimonials': testimonials_list})
