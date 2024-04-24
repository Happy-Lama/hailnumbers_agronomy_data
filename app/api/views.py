# 16/04/2024: added new view function to fetch modules and adjusted to fetch module parameters


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import Response, status
from rest_framework.decorators import api_view
from .serializers import SoilParametersSerializer, DataCollectionModuleSerializer
from .models import SoilParameters, DataCollectionModule
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
        # for key in data.keys():
        #     if key != 'timestamp':
        #         data[key] = float(data[key])
        if data:
            serializer = SoilParametersSerializer(data=data)
            
            if serializer.is_valid():
                # print(serializer.data)
                try:
                    serializer.save()
                except:
                    print("Error occurred")
                return Response(status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_parameters(request, module_id):
    try:
        module = DataCollectionModule.objects.get(module_id=module_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if module:
        start_date = request.GET.get('startDate', None)
        end_date = request.GET.get('endDate', None)
        if end_date and start_date:
            parameters = module.soilparameters_set.filter(timestamp__range = [start_date, end_date])
            serialized_parameters = SoilParametersSerializer(parameters, many=True)
            return Response(data=serialized_parameters.data, status=status.HTTP_200_OK)
        else:
            parameters = module.soilparameters_set.order_by('-timestamp')[:100]
            serialized_parameters = SoilParametersSerializer(parameters, many=True)
            return Response(data=serialized_parameters.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_modules(request):
    modules = DataCollectionModule.objects.all()
    if modules:
        serializer = DataCollectionModuleSerializer(modules, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

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