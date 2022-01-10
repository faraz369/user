from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .serializer import UserSerializer,MyTokenSerializer
from .serializer import UserCreationSerializer, UserTokenSerializer, BlogSerializer, UserSerializer
from .models import User, Blog
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET'])
@permission_classes((AllowAny,))
def User_details(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def User_Fulldetail(request):
    user = User.objects.all()
    serializer = UserSerializer(user,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
@api_view(['POST'])
@permission_classes((AllowAny,))
def Usercreation(request):
    if User.objects.filter(username=request.data['username']).exists():
        print("Username is already exists")
        return HttpResponse("Username is already exists")
    if User.objects.filter(email=request.data['email']).exists():
        print("Email is already exists")
        return HttpResponse("email is already exists")
    password = request.data['password']
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        return HttpResponse("Successfully entered")
@api_view(['POST'])
@permission_classes((AllowAny,))
def Login(request):
    serializer = UserTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(email=serializer.data.get('email'),password=serializer.data.get('password'))
        if user is not None:
            token, create_or_fetch = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
            return HttpResponse("Welcome ! Dashboard Coming Soon")
        return HttpResponse("Wrong credentials. Please try again")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Logout(request):
    request.user.auth_token.delete()
    return HttpResponse("Good Bye !")

@api_view(['DELETE'])
@permission_classes((AllowAny,))
def delete(request,pk):
    user = User.objects.get(id=pk)
    if user:
        user.delete()
        return HttpResponse("SUCCESSFULLY DELETED")
    return HttpResponse("ERROR")
@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def update(request, pk):
    if User.objects.filter(username=request.data['username']).exists():
        return HttpResponse("Username is already Exists")
    if User.objects.filter(email=request.data['email']).exists():
        return HttpResponse("Email is already Exists")
    password = request.data['password']
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserCreationSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Successfully entered")
    return HttpResponse("Serializer is not valid")

# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenSerializer

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def BlogCreation(request):
    request.data['author'] = request.user.id
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
@permission_classes((AllowAny,))
def Blog_details(request,pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def Blog_Fulldetail(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_Blogs(request):
    # author_id=request.data
    blogs = Blog.objects.filter(author_id=request.data['author_id'])
    serializer = BlogSerializer(blogs)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return Response(blogs)
    # id = request.data['id']
    # return Blog.objects.filter(author=id)
    # # user = Blog.objects.filter(author_id=request.data['id'])
    # print('3')
    # return Blog.objects.filter(author=user)
    # blogs = Blog.objects.filter(author=request.data)
    # return HttpResponse(blogs, content_type='application/json')
    # return HttpResponse(request, "articles/article_list.html", {'articles': articles})