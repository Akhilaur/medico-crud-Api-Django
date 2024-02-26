from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK ,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED
)

from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token
from . import serializers
from medical.models import medicalmedicines
from rest_framework import filters, generics
from medical import views
from . serializers import MedicineSerializer
# Create your views here.



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    
    first_name=request.data.get("first_name")
    last_name=request.data.get("last_name")
    username=request.data.get("username")
    email=request.data.get("email")
    password=request.data.get("password")
    password2=request.data.get("password2")
    if username is None or email is None or password is None or password2 is None or first_name is None or last_name is None:
        return Response({'error': 'please provide first_name , last_name, username,password,password2 and email'},status=HTTP_400_BAD_REQUEST)
    elif password!=password2:
        return Response({'error':'password is not same'},status=HTTP_400_BAD_REQUEST)
    elif User.objects.filter(username=username).exists():
        return Response({'error':'user already exist'},status=HTTP_400_BAD_REQUEST)
    else:
        user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name,)
        user.save()
        return Response({'sucess':'user created sucessfully!'},status=HTTP_201_CREATED)
        


  
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password") 
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token_obj, _ = Token.objects.get_or_create(user = user)
    return Response({'token': token_obj.key},status=HTTP_200_OK)

                                            
# UserSerializer, MedicineSerializer

@api_view(["GET"]) 
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response('User Logged out success')

class CreateMedicine(generics.CreateAPIView): 
    queryset = medicalmedicines.objects.all()
    serializer_class = serializers.MedicineSerializer 
    permission_classes = [IsAuthenticated]

class ReadMedicine(generics.ListAPIView):
    queryset = medicalmedicines.objects.all()
    serializer_class = serializers.MedicineSerializer
    permission_classes = [IsAuthenticated]

class UpdateMedicine(generics.RetrieveUpdateAPIView):
    queryset = medicalmedicines.objects.all()
    serializer_class = serializers.MedicineSerializer 
    permission_classes = [IsAuthenticated] 
    

class DeleteMedicine(generics.DestroyAPIView):
    queryset = medicalmedicines.objects.all()
    serializer_class = serializers.MedicineSerializer
    permission_classes = [IsAuthenticated]
    

class MedicineSearch(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = medicalmedicines.objects.all()
    serializer_class = serializers.MedicineSerializer
    filter_backends = [filters.SearchFilter]
   
    search_fields = ['medicine_name','company_name'] 




@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete(request, id):

    data = get_object_or_404(medicalmedicines, id=id)
    data.delete()
    return Response({"success": "Medicine deleted success"}, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def search(request):
    search = request.query_params.get('search', '')
    if search:
        allMed = medicalmedicines.objects.filter(medicine_name__istartswith=search)
        if not allMed:
            return Response({"No item with your search", search}, status=HTTP_204_NO_CONTENT)

        else:
            
            serializer = MedicineSerializer (allMed, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

  
   












