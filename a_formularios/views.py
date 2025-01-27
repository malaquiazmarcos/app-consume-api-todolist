from django.shortcuts import render, redirect
import requests
from a_formularios.forms import TodoListForm

def index(request):

    return render(request, 'base.html')

def todolist_view(request): 
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['titulo']
            description = form.cleaned_data['descripcion']
            completed = form.cleaned_data['completado']

            data = {
                'title':title,
                'description':description,
                'completed':completed
            }

            print(f' aca se imprime la data {data}')

            api_url = 'http://127.0.0.1:8001/api/tareas/'  # URL del endpoint de la API
            response = requests.post(api_url, json=data)  # solicitud GET a la API

            print(response.status_code)  # Debería ser 400
            print(response.json())  # Imprime el mensaje de error


            if response.status_code == 201:
                return redirect('envio_exitoso_view')
            else:
                print('ERROR!')

        else:
            print(form.errors)
    else: 
        form = TodoListForm()  # si es get muestra el form vacio

    return render(request, 'a_formularios/todolist.html', {'form':form})


def envio_exitoso_view(request):

    return render(request, 'a_formularios/enviado.html')


def listar_tareas_view(request):
    api_url = 'http://127.0.0.1:8001/api/tareas/'  # URL del endpoint de la API

    response = requests.get(api_url)  # solicitud GET a la API

    if response.status_code == 200:
        
        tareas = response.json()  # Convierte respuesta JSON en un diccionario de Python
        
        return render(request, 'a_formularios/listar_tareas.html', {'tareas':tareas})
    else:
        print('Ha ocurrido un error!')


def editar_tareas_view(request, id):
    api_url = f'http://127.0.0.1:8001/api/tareas/{id}/'  # URL del endpoint de la API
    response = requests.get(api_url)

    if response.status_code != 200:
        print('Error')

    tarea = response.json()

    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['titulo']
            description = form.cleaned_data['descripcion']
            completed = form.cleaned_data['completado']

            data = {
                'title':title,
                'description':description,
                'completed':completed
            }

            response = requests.put(api_url, json=data)
            if response.status_code == 200:
                print('Se ha editado con exito!')
                return redirect('listar_tareas')
            else:
                print('Ha ocurrido un error!')
    else:
        form = TodoListForm(initial={
            'titulo': tarea['title'],
            'descripcion': tarea['description'],
            'completado': tarea['completed'],
        })

    return render(request, 'a_formularios/editar_tareas.html', {
        'form':form,
        'tarea':tarea,
    })


def eliminar_tarea_view(request, id):
    api_url = f'http://127.0.0.1:8001/api/tareas/{id}/'  # URL del endpoint de la API
    response = requests.delete(api_url)

    if response.status_code == 204:
        return redirect('listar_tareas_view')
    else:
        print('Ha ocurrido un error!')







