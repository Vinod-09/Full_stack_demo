from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mobile_List, Mobile_Features
from .serializers import MobileSerializer, FeatureSerializer

@api_view(['GET'])
def get_all_data(request):
    mobile = Mobile_List.objects.all()
    serialize_mobile = MobileSerializer(mobile, many=True)
    return Response(serialize_mobile.data)

@api_view(['GET'])
def get_data_byID(request,mobile_id):
    try:
        data_by_id = Mobile_List.objects.get(id=mobile_id)
        serialize_id = MobileSerializer(data_by_id)
        return Response(serialize_id.data)
    except Mobile_List.DoesNotExist:
        return Response({'error':'Mobile not found'},status=status.HTTP_404_NOT_FOUND)


#user adds Mobile 
@api_view(['POST'])
@csrf_exempt
def add_mobile(request):
    print('=============================')
    print('data received :',request.data)
    serialize = MobileSerializer(data=request.data)
    print('==============================')
    print('serialize :: ',serialize)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    else:
        print("❌ Errors:", serialize.errors) 
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def add_new_features(request,mobile_id):
   try:
        mobile = Mobile_List.objects.get(id=mobile_id)
        data = request.data
        data['mobile'] = mobile.id
        serialize = FeatureSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
   except Mobile_List.DoesNotExist:
       return Response({'error':'Mobile not found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_data(request,mobile_id):
    try:
        mobile = Mobile_List.objects.get(id=mobile_id)
        serialize = MobileSerializer(mobile, request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_304_NOT_MODIFIED)
    except mobile.DoesNotExist:
        return Response({'error':'Mobile not found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_data(rquest,mobile_id):
   try:
    mobile = Mobile_List.objects.get(id=mobile_id)
    mobile.delete()
    return Response({'message':'Successfully deleted'},status=status.HTTP_204_NO_CONTENT)
   except mobile.DoesNotExist:
       return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)

def front_end(request):
    return render(request, 'index.html')










