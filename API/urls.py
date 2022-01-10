from django.urls import path
from .views import Login,User_Fulldetail,User_details,Usercreation,delete,update,BlogCreation,Blog_details,Blog_Fulldetail,Logout,user_Blogs

urlpatterns = [
    path('SpecificUserDetail/<int:pk>', User_details),
    path('UserCreation/', Usercreation),
    path('UserDetail/', User_Fulldetail),
    path('Login/', Login),
    path('Logout/',Logout),
    # path('Token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('RefreshToken/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('VerifyToken/', TokenVerifyView.as_view(), name='token_verify'),
    path('UserDelete/<int:pk>', delete),
    path('UserUpdate/<int:pk>',update),
    path('BlogCreation/', BlogCreation),
    path('BlogDetails/<int:pk>', Blog_details),
    path('BlogFullDetail/', Blog_Fulldetail),
    path('UserBlogs/', user_Blogs),

]