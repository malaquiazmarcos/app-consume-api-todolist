from django.urls import path
from a_formularios.views import todolist_view, index, envio_exitoso_view, listar_tareas_view, editar_tareas_view, eliminar_tarea_view

urlpatterns = [
    path('', index, name='index'),
    path('todo-list/', todolist_view, name='todolist_view'),
    path('listar-tareas/', listar_tareas_view, name='listar_tareas_view'),
    path('editar-tareas/<int:id>/', editar_tareas_view, name='editar_tareas_view'),
    path('eliminar-tareas/<int:id>/', eliminar_tarea_view, name='eliminar_tarea_view'),
]