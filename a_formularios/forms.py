from django import forms

class TodoListForm(forms.Form):
    titulo = forms.CharField(max_length=100, label='Titulo')
    descripcion = forms.CharField(
        widget=forms.Textarea,
        label='Descripción'
    )
    completado = forms.BooleanField(label='Completado', required=False)