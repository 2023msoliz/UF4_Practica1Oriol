from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def teachers(request):
    teachers = {
  "alumnos": [
    {
      "nom": "John",
      "cognom1": "Smith",
      "cognom2": "Johnson",
      "correu": "john@example.com",
      "curs": "ASIX",
      "tutor": False,
      "moduls_impartits": 3
    },
    {
      "nom": "Maria",
      "cognom1": "Garcia",
      "cognom2": "Lopez",
      "correu": "maria@example.com",
      "curs": "SMX",
      "tutor": True,
      "moduls_impartits": 5
    },
    {
      "nom": "Carlos",
      "cognom1": "Martinez",
      "cognom2": "Gomez",
      "correu": "carlos@example.com",
      "curs": "DAM",
      "tutor": False,
      "moduls_impartits": 2
    },
    {
    "nom": "Jane",
    "cognom1": "Doe",
    "cognom2": "Smith",
    "correu": "jane@itic.cat",
    "curs": "DAW",
    "tutor": True,
    "moduls_impartits": 4
  }
  ]
}

    return render(request, 'index.html', {'id': teachers["id"], 'nom': teachers["nom"], 'cognom1': teachers["cognom1"], 'cognom2': teachers["cognom2"], 'correu': teachers["correu"], 'curs': teachers["curs"], 'tutor': teachers["tutor"], 'moduls_impartits': teachers["moduls_impartits"]})
