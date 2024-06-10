from django.db import models
import uuid
# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    precio = models.CharField(max_length=20, default= "Precio: ")
    static_url = models.CharField(max_length=50, default="img/")
    
    def __str__(self):
        return f"Objeto Flan: {self.id} - {self.name}"
    

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64,)
    message = models.TextField()

    
    def __str__(self):
        return f"Formulario de Contacto: {self.id} - {self.customer_name}"
    

class FotoCarrusel(models.Model):
    name = models.CharField(max_length=50)
    static_url = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Fotos Carrusel: {self.name}"
    