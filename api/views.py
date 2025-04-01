from django.shortcuts import render,redirect, get_object_or_404
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UsuarioSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Create your views here.

def index(request):
    
    if(not "fecha_inicio" in request.session):
        request.session["fecha_inicio"] = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    return render(request, 'principal.html')


########################################################################################################################################################################


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


########################################################################################################################################################################


#Ahora vamos a crear las 4 páginas de error
def error_404_view(request, exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def error_403_view(request, exception=None):
    return render(request, 'errores/403.html', None, None, 403)

def error_400_view(request, exception=None):
    return render(request, 'errores/400.html', None, None, 400)

def error_500_view(request, exception=None):
    return render(request, 'errores/500.html', None, None,500)