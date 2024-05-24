from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mascotas(request):
    return HttpResponse("""
    <h2>¡Cat Lover!</h1>
    <p> Michis, michis, michis</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Collage_of_Six_Cats-02.jpg/905px-Collage_of_Six_Cats-02.jpg" alt="gatos_collage">
""")

def mascotas2(request):
    return render(request, 'index.html')