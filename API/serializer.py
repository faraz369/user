from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, Blog
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)


class UserCreationSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UserloginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserlogoutSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserTokenSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)

# class MyTokenSerializer(TokenObtainPairSerializer):
#     def get_token(cls , user):
#         token = super(MyTokenSerializer, cls).get_token(user)
#         token['Username'] = user.username
#         token['Email'] = user.email
#         return token


class BlogSerializer(ModelSerializer):
    # def to_representation(self, instance):
        # ret = super().to_representation(instance)
        # firstname = instance.author.firstname
        # lastname = instance.author.lastname
        # # firstname=ret['firstname']
        # # lastname = ret['lastname']
        # name = firstname +''+ lastname
        # ret['author'] = (name)
        # return retretretret
    # firstname = serializers.SerializerMethodField('get_firstname_from_author')
    # lastname = serializers.SerializerMethodField('get_lastname_from_author')
    # author = serializers.SerializerMethodField()
    # username = serializers.SerializerMethodField('get_username_from_author')
    # blogs = serializers.StringRelatedField(many=True)
    class Meta:
        model = BlogBlog
        fields = '__all__'

    # def get_firstname_from_author(self,Blog):
    #     firstname = Blog.author.firstname
    #     return firstname
    # def get_username_from_author(self,Blog):
    #     username = Blog.author.username
    #     return username
    def __str__(self):
        return self.author.username
 # def __str__(self):
    #     return self.author.username
# class BlogCreationSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['author'] = {"id": instance.author.id, "username": instance.author.username}
    #     return ret

# class PostSerializer(ModelSerializer):
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation["author"] = BlogSerializer(instance.author).data
#         return representation

    # def get_queryset(self):
    #     user = self.request.data.id
    #     return Blog.objects.filter()