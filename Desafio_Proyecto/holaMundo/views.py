from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""
                        <!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Diego">
    <meta name="description" content="Desafío Django">
    <meta name="keywords" content="front-end, framework, responsividad">
    <title>KulGym </title>
    <link rel="icon" type="image/png" href="https://cdn-icons-png.flaticon.com/512/1576/1576312.png">
    <link
        href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
        rel="stylesheet">
    <script src="https://kit.fontawesome.com/67b890a7ad.js" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
    <!--NavBar-->

    <nav class="navbar navbar-expand-lg fixed-top" data-bs-theme="dark">
        <div class="container px-5">
            <a class="navbar-brand" href="#"><img src="https://cdn-icons-png.flaticon.com/512/1576/1576312.png" alt="logo_gym" width="30em"> KulGym</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <header>
        <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="https://eurofitness.com/wp-content/uploads/2021/09/beneficios-gimnasio-gente-728.jpeg" class="d-block w-100" alt="carrusel1">
                </div>
                <div class="carousel-item">
                    <img src="https://www.65ymas.com/uploads/s1/45/11/51/bigstock-side-view-of-senior-multiethni-278365279.jpeg" class="d-block w-100" alt="carrusel2">
                </div>
                <div class="carousel-item">
                    <img src="https://uvn-brightspot.s3.amazonaws.com/assets/vixes/imj/5/5-lecciones-que-hemos-aprendido-de-las-mujeres-de-tercera-edad-en-el-gym.jpg" class="d-block w-100" alt="carrusel3">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying"
                data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying"
                data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </header>
    <footer>
        <div class="container-fluid bg-info py-4 px-4">
            <div class="row justify-content-evenly">
                <div class="col-12 col-md-2 text-center">
                    <img src="https://cdn-icons-png.flaticon.com/512/1576/1576312.png" alt="logo_gym" width="30em">
                    <p class="fs-4">KulGym</p>
                </div>
                <div class="col-12 col-md-2 text-center">
                    <a href="www.linkedin.com"><i class="fa-brands fa-linkedin icono"></i></a>
                    <a href="www.facebook.com"><i class="fa-brands fa-facebook icono"></i></a>
                    <a href="www.twitter.com"><i class="fa-brands fa-twitter icono"></i></a>
                </div>
            </div>
        </div>

    </footer>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
</body>

</html>""")
def about(request):
    return render(request, 'index1.html')
def contact(request):
    return render(request, 'index2.html')
