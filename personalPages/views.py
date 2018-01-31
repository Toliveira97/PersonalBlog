from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from . import values

def index(request):
    return resume(request)

def resume(request):
    context = {
        'fullname': values.FULL_NAME,
        'resume_pdf_url': values.RESUME_PDF_URL,
        'resume_image_url': values.RESUME_IMAGE_URL,
    }
    return render(request, 'personalPages/resume.html', context)

def about(request):
    context = {
        'fullname': values.FULL_NAME
    }
    return render(request, 'personalPages/about.html', context)