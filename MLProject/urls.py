from django.contrib import admin
from django.urls import path
from MLProject import views
urlpatterns = [
    path("",views.index,name="home"),
    path("pred",views.prednormal,name="anyuserpredict"),
    path("predict",views.predict,name="predict"),
    path("pred12mon",views.pred12month,name="predict12month"),
    path("predgraph",views.forgraphs,name="predictgraphs"),
    path("register",views.register,name="register"),
    path("login",views.loginUser,name="login"),
    path("logout",views.logoutUser,name="logout"),
    path("test",views.test,name="test"),
    path("faq",views.faq,name="faq"),
    path("questionpred",views.questionpred,name="questionpred"),
    path("about",views.about,name="about")
]