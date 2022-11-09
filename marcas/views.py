from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Marca
from .serializers import MarcaSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")



@api_view(['GET', 'POST','DELETE'])
def api_note(request, note_id):
    
    try:
        note = Marca.objects.get(id=note_id)
    except Marca.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        
        note.save()

    if request.method == 'DELETE':
        note.delete()
        # return Response(status=204)
    serialized_note = MarcaSerializer(note)
    return Response(serialized_note.data)

@api_view(['GET', 'POST'])

def api_note_list(request):

    if request.method == "POST":
        new_note_data = request.data
        title = new_note_data['title']
        content = new_note_data['content']
        note = Marca(title=title, content=content)
        note.save()

   
    notes = Marca.objects.all()

    serialized_note = MarcaSerializer(notes, many=True)
    return Response(serialized_note.data)

