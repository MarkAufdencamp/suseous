from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return HttpResponse('<html><head><title>su SEO Console</title></head><body><h1>su SEO Console</h1></body></html>')
