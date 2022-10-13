from django.urls import path
app_name =users
urlpatterns = [
    path("singup/",view.signup,name='signup'),

]