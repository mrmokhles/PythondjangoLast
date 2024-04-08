from rest_framework.response import Response
from rest_framework.decorators import api_view



from app1.models import Item
from .serializers import ItemSerializers

@api_view(['get'])
def getData(request):
    items=Item.objects.all()
    serializer=ItemSerializers(items,many=True)
    return Response(serializer.data)

@api_view(['post'])
def addItem(request):
    
    serializer=ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)