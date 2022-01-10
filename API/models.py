from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class MyAccountManager(BaseUserManager):
    def Create_user(self,first_name,lastname,email,username,password=None):
        user=self.model(first_name=first_name,lastname=lastname,email=self.normalize_email(email),username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email,password):
        user = self.Create_user(email=self.normalize_email(email), username=username, password=password,)
        user.is_admin=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return self.is_superadmin
    def has_module_perms(self, app_Label):
        return True
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=1000)
#

# class MyBlogManager(BaseUserManager):
#     def Create_Blog(self,author,title,body):
#         Blog=self.model(author=author,title=title,body=body)
#         Blog.save(using=self._db)
#         return Blog
# def get_profile_image_filepath(self,filename):
#     return f'profile_image/{self.pk}/{"profile_image.png"}'

class Blog(models.Model):
    profile_image = models.ImageField('upload image',null=True)
    # max_length = 255, upload_to = get_profile_image_filepath,
    author = models.ForeignKey(User, default=None, null=True, blank=True , on_delete=models.CASCADE)
    # User, on_delete = models.CASCADE, related_name = 'blog_posts'
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return str(self.user.username)

    # def __str__(self):
    #     """String representation"""
    #     return self.author.username

    # objects = MyBlogManager()

    def __str__(self):
        return self.title
    # def __str__(self):
    #     return self.body
    # def __str__(self):
    #     return self.profile_image
    # def __str__(self):
    #     return self.author
    # def has_module_perms(self, app_Label):
    #     return True
    # def get_profile_image_filename(self):
    #     return str(self.profile_image)[str(self.profile_image).index('profile_images/')]