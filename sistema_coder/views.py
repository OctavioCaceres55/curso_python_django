from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar(request):
    saludo = "Hola MI VIDA <3. TE AMO MUCHO. SOS HERMOSA. SOS LO MAS LINDO QUE HAY"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_fecha(request):
    hoy = datetime.now().day
    saludo = f"Hola querido usuario, fecha: {hoy} "
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html

def saludar_al_amor(request):
    saludo1 = f"Hola mi vida entera. Te amo muchísimo. Te veo el sábado"
    pagina_html = HttpResponse(saludo1)
    return pagina_html

def saludar_con_html(request):
    contexto= {}
    http_response = render(
        request=request,
        template_name='control_estudios/base.html',
        context=contexto,
    )
    return http_response





