from django.shortcuts import render
from .models import Notes


# Create your views here.
def list_notes(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notesList.html', {'notes': all_notes})
