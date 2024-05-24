from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return HttpResponse("""
                        <h1>Hola Mundo!!</h1>
                        <p> Este es un párrafo desde Django</p>
                        """)
    
def index(request):
    return HttpResponse("""
                      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>proyecto Django</title>
</head>
<body>
    <h1>Hola Mundo!!</h1>
    <p> Este es un párrafo desde Django</p>
    <ul>
        <li> primer punto</li>
        <li> segundo punto</li>
        <li> tercer punto</li>
        <li> cuarto punto</li>
    </ul>
</body>
</html>""")