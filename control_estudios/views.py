from django.shortcuts import render

def lista_de_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Lopez"},
            {"nombre": "Octavio", "apellido": "Caceres"},
            {"nombre": "Julian", "apellido": "Alvarez"}, 
        ]
    }
    http_response = render(
        request= request,
        template_name= 'control_estudios/lista_estudiantes.html',
        context = contexto,   
    )
    return http_response

def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre": "Python", "comision": "40440"},
            {"nombre": "Frontend", "comision": "1000"},
            {"nombre": "Diseño", "comision": "1001"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_responde