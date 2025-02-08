from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'astrology_app/home.html')  # Renders the homepage

def horoscope(request):
    zodiac_signs = ZodiacSign.objects.all()  # Fetch all zodiac signs dynamically
    return render(request, 'astrology_app/horoscope.html', {'zodiac_signs': zodiac_signs})

