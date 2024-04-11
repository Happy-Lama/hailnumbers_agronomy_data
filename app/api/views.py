from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import Response, status
from rest_framework.decorators import api_view
from .serializers import SoilParametersSerializer
from .models import SoilParameters
import json
from rest_framework.exceptions import APIException
# import datetime
import csv
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def add_parameters(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print("Received Data", data)
        print("Type received:", type(data))
        if data:
            serializer = SoilParametersSerializer(data=data)
            
            if serializer.is_valid():
                print(serializer.data)
                print(serializer.save())
                return Response(status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_parameters(request):
    parameters = SoilParameters.objects.all()
    serialized_parameters = SoilParametersSerializer(parameters, many=True)
    return Response(data=serialized_parameters.data, status=status.HTTP_200_OK)



def download_csv(request):
    queryset = SoilParameters.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    field_names = [field.name for field in SoilParameters._meta.fields]
    writer = csv.DictWriter(response, fieldnames=field_names)
    writer.writeheader()

    for obj in queryset:
        writer.writerow({field: getattr(obj, field) for field in field_names})

    return response