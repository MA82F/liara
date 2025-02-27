from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        user = User.objects.filter(email=email).first()
        if user is None:
            serializer.save()
            return Response({
                "message": "User signed up successfully."
            })
        return Response({
        "error": "Email is already registered."
    })
    return Response({
        "error": "Email is already registered."
    })

@api_view(['POST'])
def login(request):
    serializer = UserSerializer(data = request.data)

    if serializer.is_valid(): 
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = User.objects.get(email=email)
        if user:
            if user.password == password:
                token = get_tokens_for_user(user)
                return Response({
                    "message": "Login successful.",
                    "token": token
                })
            return Response({
        "error": "Invalid email or password."
    })
    return Response({
        "error": "Invalid email or password."
    })

    
