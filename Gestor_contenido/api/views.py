from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ContentForm
from .models import Content
from bs4 import BeautifulSoup
import json
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def render_json(request, id):
    content = get_object_or_404(Content, id=id)
    # Renderiza el HTML completo
    full_html = render(request, 'content_detail.html', {'content': content}).content
    # Utiliza BeautifulSoup para extraer solo el contenido del div container
    soup = BeautifulSoup(full_html, 'html.parser')
    # Construye el diccionario con los datos en el formato requerido
    container_div = soup.find('div', class_='container')
    # Construir la URL dinámica
    link = settings.BASE_URL + f'/content/{content.id}/'
    data = {
        "id": content.id,
        "date": content.created_at.isoformat(),
        "guid": {
            "rendered": link,
        },
        "modified": content.updated_at.isoformat() if hasattr(content, 'updated_at') else content.created_at.isoformat(),
        "slug": content.title.lower().replace(' ', '-'),
        "status": "publish",
        "type": "post",
        "link": link,
        "title": {
            "rendered": content.title
        },
        "content": {
            "rendered": str(container_div),
            "protected": False
        },
        "excerpt": {
            "rendered": content.body[:150],
            "protected": False
        }
    }

    # Retorna la respuesta en JSON
    return JsonResponse(data)
    #return render(request, 'rendered_content.html', {'data': data})

@login_required    
def content_detail(request,id):
    # Recupera el contenido específico usando el ID
    content = get_object_or_404(Content, id=id)
    return render(request, 'content_detail.html', {'content': content})

@login_required
def create_content(request, id=None):
    if id:
        content = get_object_or_404(Content, id=id)
    else:
        content = None

    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)  # Usar request.FILES para manejar imágenes
        if form.is_valid():
            form.save()  # Guarda el contenido en la base de datos
            return redirect('home')  # Redirigir a una lista de contenidos o donde prefieras
    else:
        form = ContentForm(instance=content)
    
    return render(request, 'create_content.html', {'form': form})

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content_list.html', {'contents': contents})

def listar_contenido(request):
    contenidos = Content.objects.all()
    return render(request, 'listar_contenido.html', {'contenidos': contenidos})

@login_required
def home(request):
    contenidos = Content.objects.all()
    return render(request, 'home.html', {'contenidos': contenidos})

def home2(request):
    contenidos = Content.objects.all()
    return render(request, 'home2.html', {'contenidos': contenidos})

@login_required
def delete_content(request, id):
    content = get_object_or_404(Content, id=id)
    if request.method == 'POST':
        content.delete()
        return redirect('home')  # Redirige a la lista de contenidos
    return render(request, 'confirm_delete.html', {'content': content})  # Muestra la vista de confirmación

def setup_groups(request):
    # Crear los grupos Admin y UsuarioRegular
    admin_group, _ = Group.objects.get_or_create(name="Admin")
    regular_group, _ = Group.objects.get_or_create(name="UsuarioRegular")

    # Obtener el modelo Content
    model = apps.get_model('api', 'Content')

    # Crear los permisos
    view_permission = Permission.objects.get_or_create(
        codename="can_view_all",
        name="Can view all content",
        content_type=ContentType.objects.get_for_model(model)
    )[0]

    edit_permission = Permission.objects.get_or_create(
        codename="can_edit_content",
        name="Can edit content",
        content_type=ContentType.objects.get_for_model(model)
    )[0]

    # Asignar los permisos a los grupos
    admin_group.permissions.add(view_permission, edit_permission)
    regular_group.permissions.add(view_permission)

    return HttpResponse("Grupos y permisos configurados correctamente.")

""" def redirect_to_login(request):
    if request.user.is_authenticated:
        # Redirección si el usuario está autenticado
        return redirect('home')
    else:
        # Redirección al login si no está autenticado
        return redirect('login') """