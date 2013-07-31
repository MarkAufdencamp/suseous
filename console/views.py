from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return HttpResponse('<!DOCTYPE html><html lang="en"><head><title>su SEO Console</title></head><body><h1>su SEO Console</h1><video srv="http://suseo.us/suSEOus.mov></video></body></html>')
