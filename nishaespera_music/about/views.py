from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("I am 19 years old and I major in Computer Science at Ateneo de Manila University. My music taste changes depending on my mood, but I usually like listening to pop and R&B music.")