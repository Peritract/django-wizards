# addition

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Wizard

@api_view(['GET'])
def index(request):
    return Response({"success": True,
                     "message": "Welcome to the wizard API"})

@api_view(['GET'])
def show(request):
    return Response({"success": True,
                     "wizards": [w.to_json() for w in Wizard.objects.all()]})

@api_view(['POST'])
def create(request):

    name = request.data["name"]
    type = request.data["type"]
    status = request.data["status"]

    wiz = Wizard.create(name=name, type=type, status=status)

    return Response({"success": True,
                     "wizard": wiz.to_json()})